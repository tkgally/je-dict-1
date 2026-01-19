#!/usr/bin/env python3
"""
Automated semantic tagging script for dictionary entries.

Uses pattern matching on headwords, glosses, and definitions to apply
high-confidence semantic category tags.

Usage:
    python3 build/auto_semantic_tags.py --dry-run    # Show proposed changes
    python3 build/auto_semantic_tags.py --apply      # Write changes to files
    python3 build/auto_semantic_tags.py --analyze    # Show current semantic coverage

Options:
    --dry-run   Show what would be changed without modifying files
    --apply     Apply changes to entry files
    --analyze   Analyze current semantic tag coverage
    --verbose   Show detailed output for each entry
"""

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# =============================================================================
# SEMANTIC TAG RULES
# =============================================================================
# Each rule is a tuple of (pattern_type, pattern, semantic_tags)
# pattern_type: "headword", "headword_suffix", "gloss", "gloss_exact", "reading"
# pattern: regex pattern or exact string
# semantic_tags: list of semantic tags to apply

# Days of the week
DAY_OF_WEEK_RULES = [
    ("headword_contains", "曜日", ["time-day-of-week"]),
    ("headword_contains", "曜", ["time-day-of-week"]),  # abbreviated forms
    ("gloss_exact", "Monday", ["time-day-of-week"]),
    ("gloss_exact", "Tuesday", ["time-day-of-week"]),
    ("gloss_exact", "Wednesday", ["time-day-of-week"]),
    ("gloss_exact", "Thursday", ["time-day-of-week"]),
    ("gloss_exact", "Friday", ["time-day-of-week"]),
    ("gloss_exact", "Saturday", ["time-day-of-week"]),
    ("gloss_exact", "Sunday", ["time-day-of-week"]),
]

# Months
MONTH_RULES = [
    ("gloss_exact", "January", ["time-month"]),
    ("gloss_exact", "February", ["time-month"]),
    ("gloss_exact", "March", ["time-month"]),
    ("gloss_exact", "April", ["time-month"]),
    ("gloss_exact", "May", ["time-month"]),
    ("gloss_exact", "June", ["time-month"]),
    ("gloss_exact", "July", ["time-month"]),
    ("gloss_exact", "August", ["time-month"]),
    ("gloss_exact", "September", ["time-month"]),
    ("gloss_exact", "October", ["time-month"]),
    ("gloss_exact", "November", ["time-month"]),
    ("gloss_exact", "December", ["time-month"]),
    ("headword_exact", "{一月|いちがつ}", ["time-month"]),
    ("headword_exact", "{二月|にがつ}", ["time-month"]),
    ("headword_exact", "{三月|さんがつ}", ["time-month"]),
    ("headword_exact", "{四月|しがつ}", ["time-month"]),
    ("headword_exact", "{五月|ごがつ}", ["time-month"]),
    ("headword_exact", "{六月|ろくがつ}", ["time-month"]),
    ("headword_exact", "{七月|しちがつ}", ["time-month"]),
    ("headword_exact", "{八月|はちがつ}", ["time-month"]),
    ("headword_exact", "{九月|くがつ}", ["time-month"]),
    ("headword_exact", "{十月|じゅうがつ}", ["time-month"]),
    ("headword_exact", "{十一月|じゅういちがつ}", ["time-month"]),
    ("headword_exact", "{十二月|じゅうにがつ}", ["time-month"]),
    ("reading_exact", "いちがつ", ["time-month"]),
    ("reading_exact", "にがつ", ["time-month"]),
    ("reading_exact", "さんがつ", ["time-month"]),
    ("reading_exact", "しがつ", ["time-month"]),
    ("reading_exact", "ごがつ", ["time-month"]),
    ("reading_exact", "ろくがつ", ["time-month"]),
    ("reading_exact", "しちがつ", ["time-month"]),
    ("reading_exact", "はちがつ", ["time-month"]),
    ("reading_exact", "くがつ", ["time-month"]),
    ("reading_exact", "じゅうがつ", ["time-month"]),
    ("reading_exact", "じゅういちがつ", ["time-month"]),
    ("reading_exact", "じゅうにがつ", ["time-month"]),
]

# Seasons
SEASON_RULES = [
    ("gloss_contains", "spring (season)", ["time-season"]),
    ("gloss_contains", "summer (season)", ["time-season"]),
    ("gloss_contains", "autumn (season)", ["time-season"]),
    ("gloss_contains", "fall (season)", ["time-season"]),
    ("gloss_contains", "winter (season)", ["time-season"]),
    ("reading_exact", "はる", ["time-season"]),  # needs context check
    ("reading_exact", "なつ", ["time-season"]),
    ("reading_exact", "あき", ["time-season"]),
    ("reading_exact", "ふゆ", ["time-season"]),
]

# Time periods
TIME_PERIOD_RULES = [
    ("gloss_exact", "morning", ["time-period"]),
    ("gloss_exact", "noon", ["time-period"]),
    ("gloss_exact", "afternoon", ["time-period"]),
    ("gloss_exact", "evening", ["time-period"]),
    ("gloss_exact", "night", ["time-period"]),
    ("gloss_exact", "midnight", ["time-period"]),
    ("gloss_exact", "dawn", ["time-period"]),
    ("gloss_exact", "dusk", ["time-period"]),
    ("reading_exact", "あさ", ["time-period"]),
    ("reading_exact", "ひる", ["time-period"]),
    ("reading_exact", "ごご", ["time-period"]),
    ("reading_exact", "ゆうがた", ["time-period"]),
    ("reading_exact", "よる", ["time-period"]),
    ("reading_exact", "ばん", ["time-period"]),
]

# Colors
COLOR_RULES = [
    ("gloss_exact", "red", ["color"]),
    ("gloss_exact", "blue", ["color"]),
    ("gloss_exact", "green", ["color"]),
    ("gloss_exact", "yellow", ["color"]),
    ("gloss_exact", "white", ["color"]),
    ("gloss_exact", "black", ["color"]),
    ("gloss_exact", "brown", ["color"]),
    ("gloss_exact", "orange", ["color"]),
    ("gloss_exact", "purple", ["color"]),
    ("gloss_exact", "pink", ["color"]),
    ("gloss_exact", "gray", ["color"]),
    ("gloss_exact", "grey", ["color"]),
    ("gloss_exact", "gold", ["color"]),
    ("gloss_exact", "silver", ["color"]),
    ("gloss_contains", "color", ["color"]),
    ("gloss_contains", "colour", ["color"]),
    ("reading_exact", "あか", ["color"]),
    ("reading_exact", "あお", ["color"]),
    ("reading_exact", "きいろ", ["color"]),
    ("reading_exact", "しろ", ["color"]),
    ("reading_exact", "くろ", ["color"]),
    ("reading_exact", "みどり", ["color"]),
    ("reading_exact", "ちゃいろ", ["color"]),
    ("reading_exact", "むらさき", ["color"]),
    ("reading_exact", "ピンク", ["color"]),
    ("reading_exact", "オレンジ", ["color"]),
    ("reading_exact", "グレー", ["color"]),
    ("reading_exact", "いろ", ["color"]),  # 色 itself
]

# Numbers
NUMBER_RULES = [
    ("pos_contains", "number", ["number"]),
    ("pos_contains", "counter", ["number"]),  # counters relate to numbers
    ("gloss_regex", r"^(one|two|three|four|five|six|seven|eight|nine|ten)$", ["number"]),
    ("gloss_regex", r"^\d+$", ["number"]),
    ("gloss_contains", "number", ["number"]),
]

# Directions
DIRECTION_RULES = [
    ("gloss_exact", "north", ["direction"]),
    ("gloss_exact", "south", ["direction"]),
    ("gloss_exact", "east", ["direction"]),
    ("gloss_exact", "west", ["direction"]),
    ("gloss_exact", "up", ["direction"]),
    ("gloss_exact", "down", ["direction"]),
    ("gloss_exact", "left", ["direction"]),
    ("gloss_exact", "right", ["direction"]),
    ("gloss_exact", "front", ["direction"]),
    ("gloss_exact", "back", ["direction"]),
    ("gloss_exact", "inside", ["direction"]),
    ("gloss_exact", "outside", ["direction"]),
    ("reading_exact", "きた", ["direction"]),
    ("reading_exact", "みなみ", ["direction"]),
    ("reading_exact", "ひがし", ["direction"]),
    ("reading_exact", "にし", ["direction"]),
    ("reading_exact", "うえ", ["direction"]),
    ("reading_exact", "した", ["direction"]),
    ("reading_exact", "ひだり", ["direction"]),
    ("reading_exact", "みぎ", ["direction"]),
    ("reading_exact", "まえ", ["direction"]),
    ("reading_exact", "うしろ", ["direction"]),
]

# Body parts
BODY_PART_RULES = [
    ("gloss_exact", "head", ["body-part"]),
    ("gloss_exact", "face", ["body-part"]),
    ("gloss_exact", "eye", ["body-part"]),
    ("gloss_exact", "eyes", ["body-part"]),
    ("gloss_exact", "ear", ["body-part"]),
    ("gloss_exact", "ears", ["body-part"]),
    ("gloss_exact", "nose", ["body-part"]),
    ("gloss_exact", "mouth", ["body-part"]),
    ("gloss_exact", "tooth", ["body-part"]),
    ("gloss_exact", "teeth", ["body-part"]),
    ("gloss_exact", "tongue", ["body-part"]),
    ("gloss_exact", "lip", ["body-part"]),
    ("gloss_exact", "lips", ["body-part"]),
    ("gloss_exact", "chin", ["body-part"]),
    ("gloss_exact", "cheek", ["body-part"]),
    ("gloss_exact", "neck", ["body-part"]),
    ("gloss_exact", "throat", ["body-part"]),
    ("gloss_exact", "shoulder", ["body-part"]),
    ("gloss_exact", "shoulders", ["body-part"]),
    ("gloss_exact", "arm", ["body-part"]),
    ("gloss_exact", "arms", ["body-part"]),
    ("gloss_exact", "elbow", ["body-part"]),
    ("gloss_exact", "hand", ["body-part"]),
    ("gloss_exact", "hands", ["body-part"]),
    ("gloss_exact", "finger", ["body-part"]),
    ("gloss_exact", "fingers", ["body-part"]),
    ("gloss_exact", "thumb", ["body-part"]),
    ("gloss_exact", "nail", ["body-part"]),
    ("gloss_exact", "chest", ["body-part"]),
    ("gloss_exact", "back", ["body-part"]),  # context needed
    ("gloss_exact", "stomach", ["body-part"]),
    ("gloss_exact", "belly", ["body-part"]),
    ("gloss_exact", "waist", ["body-part"]),
    ("gloss_exact", "hip", ["body-part"]),
    ("gloss_exact", "hips", ["body-part"]),
    ("gloss_exact", "leg", ["body-part"]),
    ("gloss_exact", "legs", ["body-part"]),
    ("gloss_exact", "knee", ["body-part"]),
    ("gloss_exact", "foot", ["body-part"]),
    ("gloss_exact", "feet", ["body-part"]),
    ("gloss_exact", "ankle", ["body-part"]),
    ("gloss_exact", "toe", ["body-part"]),
    ("gloss_exact", "toes", ["body-part"]),
    ("gloss_exact", "skin", ["body-part"]),
    ("gloss_exact", "hair", ["body-part"]),
    ("gloss_contains", "body part", ["body-part"]),
    ("reading_exact", "あたま", ["body-part"]),
    ("reading_exact", "かお", ["body-part"]),
    ("reading_exact", "め", ["body-part"]),
    ("reading_exact", "みみ", ["body-part"]),
    ("reading_exact", "はな", ["body-part"]),  # needs context (also flower)
    ("reading_exact", "くち", ["body-part"]),
    ("reading_exact", "は", ["body-part"]),  # needs context (also tooth)
    ("reading_exact", "した", ["body-part"]),  # tongue, but also "under"
    ("reading_exact", "くび", ["body-part"]),
    ("reading_exact", "かた", ["body-part"]),
    ("reading_exact", "うで", ["body-part"]),
    ("reading_exact", "て", ["body-part"]),
    ("reading_exact", "ゆび", ["body-part"]),
    ("reading_exact", "むね", ["body-part"]),
    ("reading_exact", "せなか", ["body-part"]),
    ("reading_exact", "おなか", ["body-part"]),
    ("reading_exact", "こし", ["body-part"]),
    ("reading_exact", "あし", ["body-part"]),
    ("reading_exact", "ひざ", ["body-part"]),
    ("reading_exact", "かみ", ["body-part"]),  # hair
]

# Family relations
FAMILY_RULES = [
    ("gloss_exact", "father", ["family"]),
    ("gloss_exact", "mother", ["family"]),
    ("gloss_exact", "parent", ["family"]),
    ("gloss_exact", "parents", ["family"]),
    ("gloss_exact", "child", ["family"]),
    ("gloss_exact", "children", ["family"]),
    ("gloss_exact", "son", ["family"]),
    ("gloss_exact", "daughter", ["family"]),
    ("gloss_exact", "brother", ["family"]),
    ("gloss_exact", "sister", ["family"]),
    ("gloss_exact", "sibling", ["family"]),
    ("gloss_exact", "siblings", ["family"]),
    ("gloss_exact", "grandfather", ["family"]),
    ("gloss_exact", "grandmother", ["family"]),
    ("gloss_exact", "grandparent", ["family"]),
    ("gloss_exact", "grandparents", ["family"]),
    ("gloss_exact", "grandchild", ["family"]),
    ("gloss_exact", "grandchildren", ["family"]),
    ("gloss_exact", "grandson", ["family"]),
    ("gloss_exact", "granddaughter", ["family"]),
    ("gloss_exact", "uncle", ["family"]),
    ("gloss_exact", "aunt", ["family"]),
    ("gloss_exact", "nephew", ["family"]),
    ("gloss_exact", "niece", ["family"]),
    ("gloss_exact", "cousin", ["family"]),
    ("gloss_exact", "husband", ["family"]),
    ("gloss_exact", "wife", ["family"]),
    ("gloss_exact", "spouse", ["family"]),
    ("gloss_contains", "older brother", ["family"]),
    ("gloss_contains", "younger brother", ["family"]),
    ("gloss_contains", "older sister", ["family"]),
    ("gloss_contains", "younger sister", ["family"]),
    ("gloss_contains", "family member", ["family"]),
    ("reading_exact", "ちち", ["family"]),
    ("reading_exact", "おとうさん", ["family"]),
    ("reading_exact", "はは", ["family"]),
    ("reading_exact", "おかあさん", ["family"]),
    ("reading_exact", "りょうしん", ["family"]),
    ("reading_exact", "こども", ["family"]),
    ("reading_exact", "むすこ", ["family"]),
    ("reading_exact", "むすめ", ["family"]),
    ("reading_exact", "あに", ["family"]),
    ("reading_exact", "おにいさん", ["family"]),
    ("reading_exact", "あね", ["family"]),
    ("reading_exact", "おねえさん", ["family"]),
    ("reading_exact", "おとうと", ["family"]),
    ("reading_exact", "いもうと", ["family"]),
    ("reading_exact", "きょうだい", ["family"]),
    ("reading_exact", "そふ", ["family"]),
    ("reading_exact", "おじいさん", ["family"]),
    ("reading_exact", "そぼ", ["family"]),
    ("reading_exact", "おばあさん", ["family"]),
    ("reading_exact", "まご", ["family"]),
    ("reading_exact", "おじ", ["family"]),
    ("reading_exact", "おば", ["family"]),
    ("reading_exact", "おっと", ["family"]),
    ("reading_exact", "つま", ["family"]),
    ("reading_exact", "かぞく", ["family"]),
]

# Animals - mammals
ANIMAL_MAMMAL_RULES = [
    ("gloss_exact", "dog", ["animal-mammal"]),
    ("gloss_exact", "cat", ["animal-mammal"]),
    ("gloss_exact", "horse", ["animal-mammal"]),
    ("gloss_exact", "cow", ["animal-mammal"]),
    ("gloss_exact", "pig", ["animal-mammal"]),
    ("gloss_exact", "sheep", ["animal-mammal"]),
    ("gloss_exact", "goat", ["animal-mammal"]),
    ("gloss_exact", "deer", ["animal-mammal"]),
    ("gloss_exact", "bear", ["animal-mammal"]),
    ("gloss_exact", "wolf", ["animal-mammal"]),
    ("gloss_exact", "fox", ["animal-mammal"]),
    ("gloss_exact", "rabbit", ["animal-mammal"]),
    ("gloss_exact", "mouse", ["animal-mammal"]),
    ("gloss_exact", "rat", ["animal-mammal"]),
    ("gloss_exact", "monkey", ["animal-mammal"]),
    ("gloss_exact", "elephant", ["animal-mammal"]),
    ("gloss_exact", "lion", ["animal-mammal"]),
    ("gloss_exact", "tiger", ["animal-mammal"]),
    ("gloss_exact", "whale", ["animal-mammal"]),
    ("gloss_exact", "dolphin", ["animal-mammal"]),
    ("reading_exact", "いぬ", ["animal-mammal"]),
    ("reading_exact", "ねこ", ["animal-mammal"]),
    ("reading_exact", "うま", ["animal-mammal"]),
    ("reading_exact", "うし", ["animal-mammal"]),
    ("reading_exact", "ぶた", ["animal-mammal"]),
    ("reading_exact", "ひつじ", ["animal-mammal"]),
    ("reading_exact", "しか", ["animal-mammal"]),
    ("reading_exact", "くま", ["animal-mammal"]),
    ("reading_exact", "おおかみ", ["animal-mammal"]),
    ("reading_exact", "きつね", ["animal-mammal"]),
    ("reading_exact", "うさぎ", ["animal-mammal"]),
    ("reading_exact", "ねずみ", ["animal-mammal"]),
    ("reading_exact", "さる", ["animal-mammal"]),
    ("reading_exact", "ぞう", ["animal-mammal"]),
]

# Animals - birds
ANIMAL_BIRD_RULES = [
    ("gloss_exact", "bird", ["animal-bird"]),
    ("gloss_exact", "crow", ["animal-bird"]),
    ("gloss_exact", "sparrow", ["animal-bird"]),
    ("gloss_exact", "pigeon", ["animal-bird"]),
    ("gloss_exact", "dove", ["animal-bird"]),
    ("gloss_exact", "eagle", ["animal-bird"]),
    ("gloss_exact", "hawk", ["animal-bird"]),
    ("gloss_exact", "owl", ["animal-bird"]),
    ("gloss_exact", "chicken", ["animal-bird"]),
    ("gloss_exact", "duck", ["animal-bird"]),
    ("gloss_exact", "crane", ["animal-bird"]),
    ("gloss_exact", "swan", ["animal-bird"]),
    ("reading_exact", "とり", ["animal-bird"]),
    ("reading_exact", "からす", ["animal-bird"]),
    ("reading_exact", "すずめ", ["animal-bird"]),
    ("reading_exact", "はと", ["animal-bird"]),
    ("reading_exact", "わし", ["animal-bird"]),
    ("reading_exact", "たか", ["animal-bird"]),
    ("reading_exact", "ふくろう", ["animal-bird"]),
    ("reading_exact", "にわとり", ["animal-bird"]),
    ("reading_exact", "あひる", ["animal-bird"]),
    ("reading_exact", "つる", ["animal-bird"]),
]

# Animals - fish
ANIMAL_FISH_RULES = [
    ("gloss_exact", "fish", ["animal-fish"]),
    ("gloss_exact", "salmon", ["animal-fish"]),
    ("gloss_exact", "tuna", ["animal-fish"]),
    ("gloss_exact", "mackerel", ["animal-fish"]),
    ("gloss_exact", "sardine", ["animal-fish"]),
    ("gloss_exact", "eel", ["animal-fish"]),
    ("gloss_exact", "shrimp", ["animal-fish"]),
    ("gloss_exact", "crab", ["animal-fish"]),
    ("gloss_exact", "octopus", ["animal-fish"]),
    ("gloss_exact", "squid", ["animal-fish"]),
    ("reading_exact", "さかな", ["animal-fish"]),
    ("reading_exact", "うお", ["animal-fish"]),
    ("reading_exact", "さけ", ["animal-fish"]),
    ("reading_exact", "まぐろ", ["animal-fish"]),
    ("reading_exact", "うなぎ", ["animal-fish"]),
    ("reading_exact", "えび", ["animal-fish"]),
    ("reading_exact", "かに", ["animal-fish"]),
    ("reading_exact", "たこ", ["animal-fish"]),
    ("reading_exact", "いか", ["animal-fish"]),
]

# Animals - insects
ANIMAL_INSECT_RULES = [
    ("gloss_exact", "insect", ["animal-insect"]),
    ("gloss_exact", "bug", ["animal-insect"]),
    ("gloss_exact", "butterfly", ["animal-insect"]),
    ("gloss_exact", "bee", ["animal-insect"]),
    ("gloss_exact", "ant", ["animal-insect"]),
    ("gloss_exact", "fly", ["animal-insect"]),
    ("gloss_exact", "mosquito", ["animal-insect"]),
    ("gloss_exact", "spider", ["animal-insect"]),
    ("gloss_exact", "dragonfly", ["animal-insect"]),
    ("gloss_exact", "cicada", ["animal-insect"]),
    ("gloss_exact", "beetle", ["animal-insect"]),
    ("reading_exact", "むし", ["animal-insect"]),
    ("reading_exact", "ちょう", ["animal-insect"]),
    ("reading_exact", "ちょうちょ", ["animal-insect"]),
    ("reading_exact", "はち", ["animal-insect"]),
    ("reading_exact", "あり", ["animal-insect"]),
    ("reading_exact", "はえ", ["animal-insect"]),
    ("reading_exact", "か", ["animal-insect"]),
    ("reading_exact", "くも", ["animal-insect"]),
    ("reading_exact", "とんぼ", ["animal-insect"]),
    ("reading_exact", "せみ", ["animal-insect"]),
]

# Plants
PLANT_RULES = [
    ("gloss_exact", "tree", ["plant-tree"]),
    ("gloss_exact", "flower", ["plant-flower"]),
    ("gloss_exact", "plant", ["plant-general"]),
    ("gloss_exact", "grass", ["plant-general"]),
    ("gloss_exact", "leaf", ["plant-general"]),
    ("gloss_exact", "leaves", ["plant-general"]),
    ("gloss_exact", "root", ["plant-general"]),
    ("gloss_exact", "seed", ["plant-general"]),
    ("gloss_exact", "cherry blossom", ["plant-flower"]),
    ("gloss_exact", "rose", ["plant-flower"]),
    ("gloss_exact", "cherry tree", ["plant-tree"]),
    ("gloss_exact", "pine tree", ["plant-tree"]),
    ("gloss_exact", "bamboo", ["plant-tree"]),
    ("reading_exact", "き", ["plant-tree"]),
    ("reading_exact", "はな", ["plant-flower"]),  # also nose
    ("reading_exact", "くさ", ["plant-general"]),
    ("reading_exact", "は", ["plant-general"]),  # leaf, also tooth
    ("reading_exact", "さくら", ["plant-flower", "plant-tree"]),
    ("reading_exact", "まつ", ["plant-tree"]),
    ("reading_exact", "たけ", ["plant-tree"]),
    ("reading_exact", "ばら", ["plant-flower"]),
]

# Weather
WEATHER_RULES = [
    ("gloss_exact", "rain", ["weather"]),
    ("gloss_exact", "snow", ["weather"]),
    ("gloss_exact", "wind", ["weather"]),
    ("gloss_exact", "cloud", ["weather"]),
    ("gloss_exact", "clouds", ["weather"]),
    ("gloss_exact", "fog", ["weather"]),
    ("gloss_exact", "thunder", ["weather"]),
    ("gloss_exact", "lightning", ["weather"]),
    ("gloss_exact", "storm", ["weather"]),
    ("gloss_exact", "typhoon", ["weather"]),
    ("gloss_exact", "sunny", ["weather"]),
    ("gloss_exact", "cloudy", ["weather"]),
    ("gloss_exact", "rainy", ["weather"]),
    ("gloss_contains", "weather", ["weather"]),
    ("reading_exact", "あめ", ["weather"]),
    ("reading_exact", "ゆき", ["weather"]),
    ("reading_exact", "かぜ", ["weather"]),
    ("reading_exact", "くも", ["weather"]),
    ("reading_exact", "きり", ["weather"]),
    ("reading_exact", "かみなり", ["weather"]),
    ("reading_exact", "たいふう", ["weather"]),
    ("reading_exact", "てんき", ["weather"]),
]

# Geography
GEOGRAPHY_RULES = [
    ("gloss_exact", "mountain", ["geography"]),
    ("gloss_exact", "river", ["geography"]),
    ("gloss_exact", "sea", ["geography"]),
    ("gloss_exact", "ocean", ["geography"]),
    ("gloss_exact", "lake", ["geography"]),
    ("gloss_exact", "island", ["geography"]),
    ("gloss_exact", "forest", ["geography"]),
    ("gloss_exact", "hill", ["geography"]),
    ("gloss_exact", "valley", ["geography"]),
    ("gloss_exact", "beach", ["geography"]),
    ("gloss_exact", "shore", ["geography"]),
    ("reading_exact", "やま", ["geography"]),
    ("reading_exact", "かわ", ["geography"]),
    ("reading_exact", "うみ", ["geography"]),
    ("reading_exact", "みずうみ", ["geography"]),
    ("reading_exact", "しま", ["geography"]),
    ("reading_exact", "もり", ["geography"]),
]

# Food and drink
FOOD_RULES = [
    ("gloss_contains", "food", ["food"]),
    ("gloss_contains", "drink", ["food"]),
    ("gloss_contains", "meal", ["food"]),
    ("gloss_exact", "rice", ["food"]),
    ("gloss_exact", "bread", ["food"]),
    ("gloss_exact", "meat", ["food"]),
    ("gloss_exact", "vegetable", ["food"]),
    ("gloss_exact", "fruit", ["food"]),
    ("gloss_exact", "water", ["food"]),
    ("gloss_exact", "tea", ["food"]),
    ("gloss_exact", "coffee", ["food"]),
    ("gloss_exact", "milk", ["food"]),
    ("gloss_exact", "alcohol", ["food"]),
    ("gloss_exact", "sake", ["food"]),
    ("gloss_exact", "beer", ["food"]),
    ("gloss_exact", "wine", ["food"]),
    ("gloss_exact", "soup", ["food"]),
    ("gloss_exact", "salt", ["food"]),
    ("gloss_exact", "sugar", ["food"]),
    ("gloss_exact", "egg", ["food"]),
    ("gloss_exact", "eggs", ["food"]),
    ("gloss_exact", "breakfast", ["food", "time-period"]),
    ("gloss_exact", "lunch", ["food", "time-period"]),
    ("gloss_exact", "dinner", ["food", "time-period"]),
    ("reading_exact", "ごはん", ["food"]),
    ("reading_exact", "パン", ["food"]),
    ("reading_exact", "にく", ["food"]),
    ("reading_exact", "やさい", ["food"]),
    ("reading_exact", "くだもの", ["food"]),
    ("reading_exact", "みず", ["food"]),
    ("reading_exact", "おちゃ", ["food"]),
    ("reading_exact", "コーヒー", ["food"]),
    ("reading_exact", "ぎゅうにゅう", ["food"]),
    ("reading_exact", "さけ", ["food"]),  # also salmon
    ("reading_exact", "ビール", ["food"]),
    ("reading_exact", "ワイン", ["food"]),
    ("reading_exact", "しお", ["food"]),
    ("reading_exact", "さとう", ["food"]),
    ("reading_exact", "たまご", ["food"]),
    ("reading_exact", "あさごはん", ["food", "time-period"]),
    ("reading_exact", "ひるごはん", ["food", "time-period"]),
    ("reading_exact", "ばんごはん", ["food", "time-period"]),
]

# Clothing
CLOTHING_RULES = [
    ("gloss_exact", "clothes", ["clothing"]),
    ("gloss_exact", "clothing", ["clothing"]),
    ("gloss_exact", "shirt", ["clothing"]),
    ("gloss_exact", "pants", ["clothing"]),
    ("gloss_exact", "trousers", ["clothing"]),
    ("gloss_exact", "skirt", ["clothing"]),
    ("gloss_exact", "dress", ["clothing"]),
    ("gloss_exact", "jacket", ["clothing"]),
    ("gloss_exact", "coat", ["clothing"]),
    ("gloss_exact", "shoes", ["clothing"]),
    ("gloss_exact", "hat", ["clothing"]),
    ("gloss_exact", "cap", ["clothing"]),
    ("gloss_exact", "socks", ["clothing"]),
    ("gloss_exact", "underwear", ["clothing"]),
    ("gloss_exact", "glasses", ["clothing"]),
    ("gloss_exact", "watch", ["clothing"]),
    ("gloss_exact", "bag", ["clothing"]),
    ("gloss_exact", "umbrella", ["clothing"]),
    ("reading_exact", "ふく", ["clothing"]),
    ("reading_exact", "シャツ", ["clothing"]),
    ("reading_exact", "ズボン", ["clothing"]),
    ("reading_exact", "スカート", ["clothing"]),
    ("reading_exact", "くつ", ["clothing"]),
    ("reading_exact", "ぼうし", ["clothing"]),
    ("reading_exact", "くつした", ["clothing"]),
    ("reading_exact", "めがね", ["clothing"]),
    ("reading_exact", "とけい", ["clothing"]),
    ("reading_exact", "かばん", ["clothing"]),
    ("reading_exact", "かさ", ["clothing"]),
]

# Buildings and places
BUILDING_RULES = [
    ("gloss_exact", "house", ["building"]),
    ("gloss_exact", "home", ["building"]),
    ("gloss_exact", "building", ["building"]),
    ("gloss_exact", "school", ["building", "education"]),
    ("gloss_exact", "hospital", ["building"]),
    ("gloss_exact", "station", ["building", "transportation"]),
    ("gloss_exact", "store", ["building"]),
    ("gloss_exact", "shop", ["building"]),
    ("gloss_exact", "restaurant", ["building", "food"]),
    ("gloss_exact", "hotel", ["building"]),
    ("gloss_exact", "bank", ["building"]),
    ("gloss_exact", "library", ["building", "education"]),
    ("gloss_exact", "temple", ["building"]),
    ("gloss_exact", "shrine", ["building"]),
    ("gloss_exact", "church", ["building"]),
    ("gloss_exact", "office", ["building", "work"]),
    ("gloss_exact", "room", ["building"]),
    ("reading_exact", "いえ", ["building"]),
    ("reading_exact", "うち", ["building"]),
    ("reading_exact", "たてもの", ["building"]),
    ("reading_exact", "がっこう", ["building", "education"]),
    ("reading_exact", "びょういん", ["building"]),
    ("reading_exact", "えき", ["building", "transportation"]),
    ("reading_exact", "みせ", ["building"]),
    ("reading_exact", "レストラン", ["building", "food"]),
    ("reading_exact", "ホテル", ["building"]),
    ("reading_exact", "ぎんこう", ["building"]),
    ("reading_exact", "としょかん", ["building", "education"]),
    ("reading_exact", "てら", ["building"]),
    ("reading_exact", "じんじゃ", ["building"]),
    ("reading_exact", "へや", ["building"]),
]

# Transportation
TRANSPORTATION_RULES = [
    ("gloss_exact", "car", ["transportation"]),
    ("gloss_exact", "train", ["transportation"]),
    ("gloss_exact", "bus", ["transportation"]),
    ("gloss_exact", "airplane", ["transportation"]),
    ("gloss_exact", "plane", ["transportation"]),
    ("gloss_exact", "ship", ["transportation"]),
    ("gloss_exact", "boat", ["transportation"]),
    ("gloss_exact", "bicycle", ["transportation"]),
    ("gloss_exact", "bike", ["transportation"]),
    ("gloss_exact", "taxi", ["transportation"]),
    ("gloss_exact", "subway", ["transportation"]),
    ("gloss_exact", "motorcycle", ["transportation"]),
    ("gloss_contains", "vehicle", ["transportation"]),
    ("reading_exact", "くるま", ["transportation"]),
    ("reading_exact", "でんしゃ", ["transportation"]),
    ("reading_exact", "バス", ["transportation"]),
    ("reading_exact", "ひこうき", ["transportation"]),
    ("reading_exact", "ふね", ["transportation"]),
    ("reading_exact", "じてんしゃ", ["transportation"]),
    ("reading_exact", "タクシー", ["transportation"]),
    ("reading_exact", "ちかてつ", ["transportation"]),
]

# Tools and everyday objects
TOOL_RULES = [
    ("gloss_exact", "pen", ["tool"]),
    ("gloss_exact", "pencil", ["tool"]),
    ("gloss_exact", "scissors", ["tool"]),
    ("gloss_exact", "key", ["tool"]),
    ("gloss_exact", "knife", ["tool"]),
    ("gloss_exact", "paper", ["tool"]),
    ("gloss_exact", "book", ["tool"]),
    ("gloss_exact", "notebook", ["tool"]),
    ("gloss_exact", "dictionary", ["tool"]),
    ("gloss_exact", "map", ["tool"]),
    ("gloss_exact", "camera", ["tool"]),
    ("gloss_exact", "clock", ["tool"]),
    ("reading_exact", "ペン", ["tool"]),
    ("reading_exact", "えんぴつ", ["tool"]),
    ("reading_exact", "はさみ", ["tool"]),
    ("reading_exact", "かぎ", ["tool"]),
    ("reading_exact", "ナイフ", ["tool"]),
    ("reading_exact", "かみ", ["tool"]),  # paper
    ("reading_exact", "ほん", ["tool"]),
    ("reading_exact", "ノート", ["tool"]),
    ("reading_exact", "じしょ", ["tool"]),
    ("reading_exact", "ちず", ["tool"]),
    ("reading_exact", "カメラ", ["tool"]),
]

# Furniture
FURNITURE_RULES = [
    ("gloss_exact", "desk", ["furniture"]),
    ("gloss_exact", "table", ["furniture"]),
    ("gloss_exact", "chair", ["furniture"]),
    ("gloss_exact", "bed", ["furniture"]),
    ("gloss_exact", "sofa", ["furniture"]),
    ("gloss_exact", "shelf", ["furniture"]),
    ("gloss_exact", "door", ["furniture"]),
    ("gloss_exact", "window", ["furniture"]),
    ("gloss_exact", "floor", ["furniture"]),
    ("gloss_exact", "wall", ["furniture"]),
    ("gloss_exact", "ceiling", ["furniture"]),
    ("reading_exact", "つくえ", ["furniture"]),
    ("reading_exact", "テーブル", ["furniture"]),
    ("reading_exact", "いす", ["furniture"]),
    ("reading_exact", "ベッド", ["furniture"]),
    ("reading_exact", "ソファー", ["furniture"]),
    ("reading_exact", "たな", ["furniture"]),
    ("reading_exact", "ドア", ["furniture"]),
    ("reading_exact", "まど", ["furniture"]),
    ("reading_exact", "ゆか", ["furniture"]),
    ("reading_exact", "かべ", ["furniture"]),
]

# Electronics
ELECTRONICS_RULES = [
    ("gloss_exact", "telephone", ["electronics"]),
    ("gloss_exact", "phone", ["electronics"]),
    ("gloss_exact", "television", ["electronics"]),
    ("gloss_exact", "TV", ["electronics"]),
    ("gloss_exact", "computer", ["electronics"]),
    ("gloss_exact", "radio", ["electronics"]),
    ("gloss_exact", "smartphone", ["electronics"]),
    ("gloss_contains", "electric", ["electronics"]),
    ("gloss_contains", "electronic", ["electronics"]),
    ("reading_exact", "でんわ", ["electronics"]),
    ("reading_exact", "テレビ", ["electronics"]),
    ("reading_exact", "パソコン", ["electronics"]),
    ("reading_exact", "コンピューター", ["electronics"]),
    ("reading_exact", "ラジオ", ["electronics"]),
    ("reading_exact", "スマホ", ["electronics"]),
    ("reading_exact", "けいたい", ["electronics"]),
]

# Emotions
EMOTION_RULES = [
    ("gloss_exact", "happy", ["emotion"]),
    ("gloss_exact", "sad", ["emotion"]),
    ("gloss_exact", "angry", ["emotion"]),
    ("gloss_exact", "fear", ["emotion"]),
    ("gloss_exact", "afraid", ["emotion"]),
    ("gloss_exact", "surprised", ["emotion"]),
    ("gloss_exact", "worried", ["emotion"]),
    ("gloss_exact", "excited", ["emotion"]),
    ("gloss_exact", "lonely", ["emotion"]),
    ("gloss_exact", "embarrassed", ["emotion"]),
    ("gloss_exact", "love", ["emotion"]),
    ("gloss_exact", "hate", ["emotion"]),
    ("gloss_exact", "joy", ["emotion"]),
    ("gloss_exact", "anger", ["emotion"]),
    ("gloss_exact", "sadness", ["emotion"]),
    ("gloss_exact", "happiness", ["emotion"]),
    ("gloss_contains", "feeling", ["emotion"]),
    ("gloss_contains", "emotion", ["emotion"]),
    ("reading_exact", "うれしい", ["emotion"]),
    ("reading_exact", "かなしい", ["emotion"]),
    ("reading_exact", "おこる", ["emotion"]),
    ("reading_exact", "こわい", ["emotion"]),
    ("reading_exact", "さびしい", ["emotion"]),
    ("reading_exact", "はずかしい", ["emotion"]),
    ("reading_exact", "あい", ["emotion"]),
    ("reading_exact", "きもち", ["emotion"]),
]

# Greetings and social expressions
GREETING_RULES = [
    ("gloss_contains", "greeting", ["greeting"]),
    ("gloss_contains", "hello", ["greeting"]),
    ("gloss_contains", "goodbye", ["greeting"]),
    ("gloss_contains", "good morning", ["greeting"]),
    ("gloss_contains", "good evening", ["greeting"]),
    ("gloss_contains", "good night", ["greeting"]),
    ("gloss_contains", "thank you", ["greeting"]),
    ("gloss_contains", "sorry", ["greeting"]),
    ("gloss_contains", "excuse me", ["greeting"]),
    ("gloss_contains", "please", ["greeting"]),
    ("gloss_contains", "welcome", ["greeting"]),
    ("reading_exact", "おはよう", ["greeting"]),
    ("reading_exact", "こんにちは", ["greeting"]),
    ("reading_exact", "こんばんは", ["greeting"]),
    ("reading_exact", "おやすみ", ["greeting"]),
    ("reading_exact", "おやすみなさい", ["greeting"]),
    ("reading_exact", "さようなら", ["greeting"]),
    ("reading_exact", "ありがとう", ["greeting"]),
    ("reading_exact", "すみません", ["greeting"]),
    ("reading_exact", "ごめん", ["greeting"]),
    ("reading_exact", "ごめんなさい", ["greeting"]),
    ("reading_exact", "いただきます", ["greeting"]),
    ("reading_exact", "ごちそうさま", ["greeting"]),
    ("reading_exact", "おねがいします", ["greeting"]),
    ("reading_exact", "よろしく", ["greeting"]),
]

# Occupations
OCCUPATION_RULES = [
    ("gloss_exact", "teacher", ["occupation"]),
    ("gloss_exact", "student", ["occupation", "education"]),
    ("gloss_exact", "doctor", ["occupation"]),
    ("gloss_exact", "nurse", ["occupation"]),
    ("gloss_exact", "police officer", ["occupation"]),
    ("gloss_exact", "policeman", ["occupation"]),
    ("gloss_exact", "lawyer", ["occupation"]),
    ("gloss_exact", "engineer", ["occupation"]),
    ("gloss_exact", "company employee", ["occupation", "work"]),
    ("gloss_exact", "cook", ["occupation", "food"]),
    ("gloss_exact", "chef", ["occupation", "food"]),
    ("gloss_exact", "driver", ["occupation", "transportation"]),
    ("gloss_exact", "artist", ["occupation"]),
    ("gloss_exact", "writer", ["occupation"]),
    ("gloss_exact", "singer", ["occupation"]),
    ("gloss_exact", "actor", ["occupation"]),
    ("gloss_contains", "profession", ["occupation"]),
    ("gloss_contains", "job", ["occupation", "work"]),
    ("reading_exact", "せんせい", ["occupation"]),
    ("reading_exact", "がくせい", ["occupation", "education"]),
    ("reading_exact", "いしゃ", ["occupation"]),
    ("reading_exact", "かんごし", ["occupation"]),
    ("reading_exact", "けいさつかん", ["occupation"]),
    ("reading_exact", "べんごし", ["occupation"]),
    ("reading_exact", "かいしゃいん", ["occupation", "work"]),
]

# Movement verbs
MOVEMENT_RULES = [
    ("gloss_exact", "to go", ["movement"]),
    ("gloss_exact", "to come", ["movement"]),
    ("gloss_exact", "to walk", ["movement"]),
    ("gloss_exact", "to run", ["movement"]),
    ("gloss_exact", "to swim", ["movement"]),
    ("gloss_exact", "to fly", ["movement"]),
    ("gloss_exact", "to return", ["movement"]),
    ("gloss_exact", "to enter", ["movement"]),
    ("gloss_exact", "to exit", ["movement"]),
    ("gloss_exact", "to leave", ["movement"]),
    ("gloss_exact", "to arrive", ["movement"]),
    ("gloss_exact", "to climb", ["movement"]),
    ("gloss_exact", "to descend", ["movement"]),
    ("gloss_contains", "to move", ["movement"]),
    ("reading_exact", "いく", ["movement"]),
    ("reading_exact", "くる", ["movement"]),
    ("reading_exact", "あるく", ["movement"]),
    ("reading_exact", "はしる", ["movement"]),
    ("reading_exact", "およぐ", ["movement"]),
    ("reading_exact", "とぶ", ["movement"]),
    ("reading_exact", "かえる", ["movement"]),
    ("reading_exact", "はいる", ["movement"]),
    ("reading_exact", "でる", ["movement"]),
    ("reading_exact", "つく", ["movement"]),
    ("reading_exact", "のぼる", ["movement"]),
    ("reading_exact", "おりる", ["movement"]),
]

# Communication verbs
COMMUNICATION_RULES = [
    ("gloss_exact", "to speak", ["communication"]),
    ("gloss_exact", "to talk", ["communication"]),
    ("gloss_exact", "to say", ["communication"]),
    ("gloss_exact", "to tell", ["communication"]),
    ("gloss_exact", "to ask", ["communication"]),
    ("gloss_exact", "to answer", ["communication"]),
    ("gloss_exact", "to read", ["communication"]),
    ("gloss_exact", "to write", ["communication"]),
    ("gloss_exact", "to listen", ["communication"]),
    ("gloss_exact", "to hear", ["communication"]),
    ("gloss_exact", "to call", ["communication"]),
    ("gloss_contains", "to communicate", ["communication"]),
    ("reading_exact", "はなす", ["communication"]),
    ("reading_exact", "いう", ["communication"]),
    ("reading_exact", "きく", ["communication"]),
    ("reading_exact", "よむ", ["communication"]),
    ("reading_exact", "かく", ["communication"]),
    ("reading_exact", "こたえる", ["communication"]),
    ("reading_exact", "よぶ", ["communication"]),
]

# Cognition verbs
COGNITION_RULES = [
    ("gloss_exact", "to think", ["cognition"]),
    ("gloss_exact", "to know", ["cognition"]),
    ("gloss_exact", "to understand", ["cognition"]),
    ("gloss_exact", "to remember", ["cognition"]),
    ("gloss_exact", "to forget", ["cognition"]),
    ("gloss_exact", "to learn", ["cognition", "education"]),
    ("gloss_exact", "to study", ["cognition", "education"]),
    ("gloss_exact", "to believe", ["cognition"]),
    ("gloss_exact", "to decide", ["cognition"]),
    ("gloss_exact", "to consider", ["cognition"]),
    ("reading_exact", "おもう", ["cognition"]),
    ("reading_exact", "しる", ["cognition"]),
    ("reading_exact", "わかる", ["cognition"]),
    ("reading_exact", "おぼえる", ["cognition"]),
    ("reading_exact", "わすれる", ["cognition"]),
    ("reading_exact", "ならう", ["cognition", "education"]),
    ("reading_exact", "べんきょうする", ["cognition", "education"]),
    ("reading_exact", "かんがえる", ["cognition"]),
    ("reading_exact", "きめる", ["cognition"]),
]

# Existence verbs
EXISTENCE_RULES = [
    ("gloss_contains", "to exist", ["existence"]),
    ("gloss_contains", "to be (location)", ["existence"]),
    ("gloss_contains", "to have", ["existence"]),
    ("gloss_contains", "to become", ["existence"]),
    ("reading_exact", "ある", ["existence"]),
    ("reading_exact", "いる", ["existence"]),
    ("reading_exact", "なる", ["existence"]),
    ("reading_exact", "もつ", ["existence"]),
]

# Consumption verbs
CONSUMPTION_RULES = [
    ("gloss_exact", "to eat", ["consumption"]),
    ("gloss_exact", "to drink", ["consumption"]),
    ("gloss_exact", "to use", ["consumption"]),
    ("gloss_exact", "to buy", ["consumption"]),
    ("gloss_exact", "to sell", ["consumption"]),
    ("reading_exact", "たべる", ["consumption"]),
    ("reading_exact", "のむ", ["consumption"]),
    ("reading_exact", "つかう", ["consumption"]),
    ("reading_exact", "かう", ["consumption"]),
    ("reading_exact", "うる", ["consumption"]),
]

# Work-related
WORK_RULES = [
    ("gloss_exact", "work", ["work"]),
    ("gloss_exact", "company", ["work"]),
    ("gloss_exact", "meeting", ["work"]),
    ("gloss_exact", "business", ["work"]),
    ("gloss_contains", "to work", ["work"]),
    ("reading_exact", "しごと", ["work"]),
    ("reading_exact", "かいしゃ", ["work"]),
    ("reading_exact", "かいぎ", ["work"]),
    ("reading_exact", "はたらく", ["work"]),
]

# Education
EDUCATION_RULES = [
    ("gloss_exact", "education", ["education"]),
    ("gloss_exact", "class", ["education"]),
    ("gloss_exact", "lesson", ["education"]),
    ("gloss_exact", "exam", ["education"]),
    ("gloss_exact", "test", ["education"]),
    ("gloss_exact", "homework", ["education"]),
    ("gloss_exact", "university", ["education", "building"]),
    ("gloss_exact", "college", ["education", "building"]),
    ("gloss_contains", "school", ["education"]),
    ("reading_exact", "きょういく", ["education"]),
    ("reading_exact", "じゅぎょう", ["education"]),
    ("reading_exact", "しけん", ["education"]),
    ("reading_exact", "テスト", ["education"]),
    ("reading_exact", "しゅくだい", ["education"]),
    ("reading_exact", "だいがく", ["education", "building"]),
]

# Leisure
LEISURE_RULES = [
    ("gloss_exact", "to play", ["leisure"]),
    ("gloss_exact", "movie", ["leisure"]),
    ("gloss_exact", "music", ["leisure"]),
    ("gloss_exact", "sport", ["leisure"]),
    ("gloss_exact", "sports", ["leisure"]),
    ("gloss_exact", "game", ["leisure"]),
    ("gloss_exact", "hobby", ["leisure"]),
    ("gloss_exact", "travel", ["leisure"]),
    ("gloss_exact", "trip", ["leisure"]),
    ("gloss_exact", "vacation", ["leisure"]),
    ("reading_exact", "あそぶ", ["leisure"]),
    ("reading_exact", "えいが", ["leisure"]),
    ("reading_exact", "おんがく", ["leisure"]),
    ("reading_exact", "スポーツ", ["leisure"]),
    ("reading_exact", "ゲーム", ["leisure"]),
    ("reading_exact", "しゅみ", ["leisure"]),
    ("reading_exact", "りょこう", ["leisure"]),
]

# Person types
PERSON_RULES = [
    ("gloss_exact", "person", ["person"]),
    ("gloss_exact", "people", ["person"]),
    ("gloss_exact", "man", ["person"]),
    ("gloss_exact", "woman", ["person"]),
    ("gloss_exact", "boy", ["person"]),
    ("gloss_exact", "girl", ["person"]),
    ("gloss_exact", "adult", ["person"]),
    ("gloss_exact", "baby", ["person"]),
    ("gloss_exact", "friend", ["person"]),
    ("reading_exact", "ひと", ["person"]),
    ("reading_exact", "にんげん", ["person"]),
    ("reading_exact", "おとこ", ["person"]),
    ("reading_exact", "おんな", ["person"]),
    ("reading_exact", "おとこのこ", ["person"]),
    ("reading_exact", "おんなのこ", ["person"]),
    ("reading_exact", "おとな", ["person"]),
    ("reading_exact", "あかちゃん", ["person"]),
    ("reading_exact", "ともだち", ["person"]),
]

# Time general
TIME_GENERAL_RULES = [
    ("gloss_exact", "time", ["time-general"]),
    ("gloss_exact", "hour", ["time-general"]),
    ("gloss_exact", "minute", ["time-general"]),
    ("gloss_exact", "second", ["time-general"]),
    ("gloss_exact", "day", ["time-general"]),
    ("gloss_exact", "week", ["time-general"]),
    ("gloss_exact", "month", ["time-general"]),
    ("gloss_exact", "year", ["time-general"]),
    ("gloss_exact", "today", ["time-general"]),
    ("gloss_exact", "tomorrow", ["time-general"]),
    ("gloss_exact", "yesterday", ["time-general"]),
    ("gloss_exact", "now", ["time-general"]),
    ("gloss_exact", "later", ["time-general"]),
    ("gloss_exact", "before", ["time-general"]),
    ("gloss_exact", "after", ["time-general"]),
    ("gloss_exact", "always", ["time-general"]),
    ("gloss_exact", "sometimes", ["time-general"]),
    ("gloss_exact", "never", ["time-general"]),
    ("reading_exact", "じかん", ["time-general"]),
    ("reading_exact", "じ", ["time-general"]),
    ("reading_exact", "ふん", ["time-general"]),
    ("reading_exact", "びょう", ["time-general"]),
    ("reading_exact", "ひ", ["time-general"]),
    ("reading_exact", "しゅう", ["time-general"]),
    ("reading_exact", "つき", ["time-general"]),
    ("reading_exact", "とし", ["time-general"]),
    ("reading_exact", "ねん", ["time-general"]),
    ("reading_exact", "きょう", ["time-general"]),
    ("reading_exact", "あした", ["time-general"]),
    ("reading_exact", "きのう", ["time-general"]),
    ("reading_exact", "いま", ["time-general"]),
    ("reading_exact", "あと", ["time-general"]),
    ("reading_exact", "まえ", ["time-general"]),
    ("reading_exact", "いつも", ["time-general"]),
    ("reading_exact", "ときどき", ["time-general"]),
]

# Size and quantity
SIZE_RULES = [
    ("gloss_exact", "big", ["size"]),
    ("gloss_exact", "large", ["size"]),
    ("gloss_exact", "small", ["size"]),
    ("gloss_exact", "long", ["size"]),
    ("gloss_exact", "short", ["size"]),
    ("gloss_exact", "tall", ["size"]),
    ("gloss_exact", "wide", ["size"]),
    ("gloss_exact", "narrow", ["size"]),
    ("gloss_exact", "thick", ["size"]),
    ("gloss_exact", "thin", ["size"]),
    ("gloss_exact", "heavy", ["size"]),
    ("gloss_exact", "light", ["size"]),
    ("reading_exact", "おおきい", ["size"]),
    ("reading_exact", "ちいさい", ["size"]),
    ("reading_exact", "ながい", ["size"]),
    ("reading_exact", "みじかい", ["size"]),
    ("reading_exact", "たかい", ["size"]),
    ("reading_exact", "ひくい", ["size"]),
    ("reading_exact", "ひろい", ["size"]),
    ("reading_exact", "せまい", ["size"]),
    ("reading_exact", "あつい", ["size"]),
    ("reading_exact", "うすい", ["size"]),
    ("reading_exact", "おもい", ["size"]),
    ("reading_exact", "かるい", ["size"]),
]

QUANTITY_RULES = [
    ("gloss_exact", "many", ["quantity"]),
    ("gloss_exact", "much", ["quantity"]),
    ("gloss_exact", "few", ["quantity"]),
    ("gloss_exact", "little", ["quantity"]),
    ("gloss_exact", "all", ["quantity"]),
    ("gloss_exact", "every", ["quantity"]),
    ("gloss_exact", "some", ["quantity"]),
    ("gloss_exact", "no", ["quantity"]),
    ("gloss_exact", "none", ["quantity"]),
    ("reading_exact", "おおい", ["quantity"]),
    ("reading_exact", "すくない", ["quantity"]),
    ("reading_exact", "ぜんぶ", ["quantity"]),
    ("reading_exact", "すべて", ["quantity"]),
]

# Combine all rules
ALL_RULES = (
    DAY_OF_WEEK_RULES +
    MONTH_RULES +
    SEASON_RULES +
    TIME_PERIOD_RULES +
    TIME_GENERAL_RULES +
    COLOR_RULES +
    NUMBER_RULES +
    DIRECTION_RULES +
    SIZE_RULES +
    QUANTITY_RULES +
    BODY_PART_RULES +
    FAMILY_RULES +
    PERSON_RULES +
    OCCUPATION_RULES +
    ANIMAL_MAMMAL_RULES +
    ANIMAL_BIRD_RULES +
    ANIMAL_FISH_RULES +
    ANIMAL_INSECT_RULES +
    PLANT_RULES +
    WEATHER_RULES +
    GEOGRAPHY_RULES +
    FOOD_RULES +
    CLOTHING_RULES +
    BUILDING_RULES +
    TRANSPORTATION_RULES +
    TOOL_RULES +
    FURNITURE_RULES +
    ELECTRONICS_RULES +
    EMOTION_RULES +
    GREETING_RULES +
    MOVEMENT_RULES +
    COMMUNICATION_RULES +
    COGNITION_RULES +
    EXISTENCE_RULES +
    CONSUMPTION_RULES +
    WORK_RULES +
    EDUCATION_RULES +
    LEISURE_RULES
)


def strip_furigana(text: str) -> str:
    """Remove furigana markup from text. {漢字|かんじ} -> 漢字"""
    return re.sub(r"\{([^|]+)\|[^}]+\}", r"\1", text)


def match_rule(entry: dict, rule: tuple) -> bool:
    """Check if an entry matches a rule."""
    pattern_type, pattern, _ = rule

    headword = entry.get("headword", "")
    reading = entry.get("reading", "")
    gloss = entry.get("gloss", "")
    pos = entry.get("part_of_speech", "").lower()

    # Strip furigana from headword for matching
    headword_plain = strip_furigana(headword)

    if pattern_type == "headword_exact":
        return headword == pattern or headword_plain == strip_furigana(pattern)

    elif pattern_type == "headword_contains":
        return pattern in headword or pattern in headword_plain

    elif pattern_type == "reading_exact":
        return reading == pattern

    elif pattern_type == "reading_contains":
        return pattern in reading

    elif pattern_type == "gloss_exact":
        # Match if gloss equals pattern (case insensitive)
        return gloss.lower() == pattern.lower()

    elif pattern_type == "gloss_contains":
        # Match if pattern is contained in gloss (case insensitive)
        return pattern.lower() in gloss.lower()

    elif pattern_type == "gloss_regex":
        return bool(re.search(pattern, gloss, re.IGNORECASE))

    elif pattern_type == "pos_contains":
        return pattern.lower() in pos

    return False


def get_semantic_tags(entry: dict) -> list[str]:
    """Get semantic tags for an entry based on all rules."""
    tags = set()

    for rule in ALL_RULES:
        if match_rule(entry, rule):
            tags.update(rule[2])

    return sorted(list(tags))


def analyze_entries(project_root: Path) -> dict:
    """Analyze semantic tag coverage across all entries."""
    entries_dir = project_root / "entries"

    stats = {
        "total": 0,
        "with_semantic": 0,
        "without_semantic": 0,
        "tag_counts": Counter(),
        "entries_by_tag": defaultdict(list),
    }

    for file_path in sorted(entries_dir.glob("**/*.json")):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                entry = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        stats["total"] += 1

        # Check existing semantic tags
        existing = entry.get("metadata", {}).get("tags", {}).get("semantic", [])
        if existing:
            stats["with_semantic"] += 1
            for tag in existing:
                stats["tag_counts"][tag] += 1
        else:
            stats["without_semantic"] += 1

            # Check what tags would be assigned
            suggested = get_semantic_tags(entry)
            if suggested:
                for tag in suggested:
                    stats["entries_by_tag"][tag].append(
                        (file_path.name, entry.get("headword", ""), entry.get("gloss", ""))
                    )

    return stats


def migrate_entry(entry: dict) -> tuple[dict, dict]:
    """Add semantic tags to an entry."""
    changes = {}

    # Get suggested tags
    semantic_tags = get_semantic_tags(entry)

    if not semantic_tags:
        return entry, changes

    # Initialize metadata.tags if needed
    if "metadata" not in entry:
        entry["metadata"] = {}
    if "tags" not in entry["metadata"]:
        entry["metadata"]["tags"] = {}

    # Only add if not already present
    existing = entry["metadata"]["tags"].get("semantic", [])
    if not existing:
        entry["metadata"]["tags"]["semantic"] = semantic_tags
        changes["semantic"] = semantic_tags

        # Update modified timestamp
        entry["metadata"]["modified"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    return entry, changes


def migrate_all_entries(
    project_root: Path,
    dry_run: bool = True,
    verbose: bool = False
) -> dict:
    """Add semantic tags to all entries."""
    entries_dir = project_root / "entries"

    stats = {
        "total": 0,
        "tagged": 0,
        "already_tagged": 0,
        "no_match": 0,
        "errors": 0,
        "tag_counts": Counter(),
    }

    for file_path in sorted(entries_dir.glob("**/*.json")):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                entry = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading {file_path}: {e}")
            stats["errors"] += 1
            continue

        stats["total"] += 1

        # Check if already has semantic tags
        existing = entry.get("metadata", {}).get("tags", {}).get("semantic", [])
        if existing:
            stats["already_tagged"] += 1
            if verbose:
                print(f"  Skip (already tagged): {file_path.name}")
            continue

        # Migrate
        migrated_entry, changes = migrate_entry(entry)

        if not changes:
            stats["no_match"] += 1
            if verbose:
                hw = entry.get("headword", "")
                gl = entry.get("gloss", "")
                print(f"  No match: {file_path.name} - {hw} ({gl})")
            continue

        stats["tagged"] += 1
        for tag in changes.get("semantic", []):
            stats["tag_counts"][tag] += 1

        if verbose or dry_run:
            rel_path = file_path.relative_to(project_root)
            hw = entry.get("headword", "")
            gl = entry.get("gloss", "")
            print(f"  {rel_path}: {hw} ({gl}) -> {changes.get('semantic', [])}")

        # Write if not dry run
        if not dry_run:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(migrated_entry, f, ensure_ascii=False, indent=2)

    return stats


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Auto-tag dictionary entries with semantic categories"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying files"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes to entry files"
    )
    parser.add_argument(
        "--analyze",
        action="store_true",
        help="Analyze current semantic tag coverage"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output"
    )
    args = parser.parse_args()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    if not (args.dry_run or args.apply or args.analyze):
        print("Error: Must specify --dry-run, --apply, or --analyze")
        parser.print_help()
        return 1

    if args.analyze:
        print("Analyzing semantic tag coverage...")
        print("-" * 60)

        stats = analyze_entries(project_root)

        print(f"\nTotal entries: {stats['total']}")
        print(f"With semantic tags: {stats['with_semantic']} ({100*stats['with_semantic']/stats['total']:.1f}%)")
        print(f"Without semantic tags: {stats['without_semantic']} ({100*stats['without_semantic']/stats['total']:.1f}%)")

        if stats["tag_counts"]:
            print(f"\nExisting tag distribution:")
            for tag, count in stats["tag_counts"].most_common():
                print(f"  {tag}: {count}")

        if stats["entries_by_tag"]:
            print(f"\nPotential tags for untagged entries:")
            for tag, entries in sorted(stats["entries_by_tag"].items()):
                print(f"\n  {tag} ({len(entries)} entries):")
                for fname, hw, gl in entries[:5]:
                    print(f"    - {fname}: {hw} ({gl[:40]}...)" if len(gl) > 40 else f"    - {fname}: {hw} ({gl})")
                if len(entries) > 5:
                    print(f"    ... and {len(entries) - 5} more")

        return 0

    # Migration mode
    mode = "DRY RUN" if args.dry_run else "APPLY"
    print(f"Semantic Tag Migration ({mode})")
    print("=" * 60)
    print(f"Project root: {project_root}\n")

    stats = migrate_all_entries(
        project_root,
        dry_run=args.dry_run,
        verbose=args.verbose
    )

    print("\n" + "=" * 60)
    print("Migration Summary")
    print("-" * 60)
    print(f"Total entries:     {stats['total']}")
    print(f"Already tagged:    {stats['already_tagged']}")
    print(f"Newly tagged:      {stats['tagged']}")
    print(f"No match:          {stats['no_match']}")
    print(f"Errors:            {stats['errors']}")

    if stats["tag_counts"]:
        print(f"\nTag distribution:")
        for tag, count in stats["tag_counts"].most_common(20):
            print(f"  {tag}: {count}")

    coverage = (stats['already_tagged'] + stats['tagged']) / stats['total'] * 100 if stats['total'] > 0 else 0
    print(f"\nSemantic coverage: {coverage:.1f}%")

    if args.dry_run and stats["tagged"] > 0:
        print(f"\nTo apply these changes, run: python3 {sys.argv[0]} --apply")

    return 0


if __name__ == "__main__":
    sys.exit(main())
