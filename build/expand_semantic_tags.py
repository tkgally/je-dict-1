#!/usr/bin/env python3
"""
Expanded semantic tagging script for dictionary entries.

This script applies broader semantic tags to entries not caught by
auto_semantic_tags.py. It uses definition analysis and POS-based
categorization to achieve >95% coverage.

Usage:
    python3 build/expand_semantic_tags.py --dry-run
    python3 build/expand_semantic_tags.py --apply
"""

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# =============================================================================
# EXPANDED SEMANTIC TAG RULES
# =============================================================================
# These are broader patterns for common categories

# Gloss-contains patterns (substring matching in gloss)
GLOSS_CONTAINS_RULES = [
    # More food items
    ("soup", ["food"]),
    ("sauce", ["food"]),
    ("noodle", ["food"]),
    ("sushi", ["food"]),
    ("ramen", ["food"]),
    ("udon", ["food"]),
    ("soba", ["food"]),
    ("tempura", ["food"]),
    ("tofu", ["food"]),
    ("miso", ["food"]),
    ("soy", ["food"]),
    ("wasabi", ["food"]),
    ("seaweed", ["food"]),
    ("onigiri", ["food"]),
    ("bento", ["food"]),
    ("snack", ["food"]),
    ("candy", ["food"]),
    ("cake", ["food"]),
    ("dessert", ["food"]),
    ("ice cream", ["food"]),
    ("chocolate", ["food"]),
    ("cookie", ["food"]),
    ("pizza", ["food"]),
    ("sandwich", ["food"]),
    ("salad", ["food"]),
    ("steak", ["food"]),
    ("chicken", ["food"]),
    ("pork", ["food"]),
    ("beef", ["food"]),
    ("lamb", ["food"]),
    ("mutton", ["food"]),
    ("bacon", ["food"]),
    ("ham", ["food"]),
    ("sausage", ["food"]),
    ("seafood", ["food"]),
    ("curry", ["food"]),
    ("juice", ["food"]),
    ("soda", ["food"]),
    ("lemonade", ["food"]),
    ("cocktail", ["food"]),
    ("wine", ["food"]),
    ("beer", ["food"]),
    ("whisky", ["food"]),
    ("whiskey", ["food"]),
    ("vodka", ["food"]),
    ("liquor", ["food"]),
    ("alcohol", ["food"]),
    ("champagne", ["food"]),
    ("coffee", ["food"]),
    ("tea", ["food"]),
    ("cocoa", ["food"]),
    ("latte", ["food"]),
    ("espresso", ["food"]),
    ("cooking", ["food"]),
    ("baking", ["food"]),
    ("frying", ["food"]),
    ("boiling", ["food"]),
    ("steaming", ["food"]),
    ("grilling", ["food"]),
    ("roasting", ["food"]),
    ("ingredient", ["food"]),
    ("recipe", ["food"]),
    ("kitchen", ["food", "building"]),
    ("restaurant", ["food", "building"]),
    ("cafe", ["food", "building"]),
    ("cafeteria", ["food", "building"]),

    # More clothing
    ("t-shirt", ["clothing"]),
    ("sweater", ["clothing"]),
    ("hoodie", ["clothing"]),
    ("jeans", ["clothing"]),
    ("blouse", ["clothing"]),
    ("suit", ["clothing"]),
    ("tuxedo", ["clothing"]),
    ("kimono", ["clothing"]),
    ("yukata", ["clothing"]),
    ("uniform", ["clothing"]),
    ("costume", ["clothing"]),
    ("pajamas", ["clothing"]),
    ("underwear", ["clothing"]),
    ("bra", ["clothing"]),
    ("panties", ["clothing"]),
    ("boxers", ["clothing"]),
    ("briefs", ["clothing"]),
    ("sock", ["clothing"]),
    ("stocking", ["clothing"]),
    ("tights", ["clothing"]),
    ("glove", ["clothing"]),
    ("scarf", ["clothing"]),
    ("tie", ["clothing"]),
    ("necktie", ["clothing"]),
    ("belt", ["clothing"]),
    ("suspender", ["clothing"]),
    ("sandal", ["clothing"]),
    ("boot", ["clothing"]),
    ("sneaker", ["clothing"]),
    ("heel", ["clothing"]),
    ("slipper", ["clothing"]),
    ("backpack", ["clothing"]),
    ("purse", ["clothing"]),
    ("wallet", ["clothing"]),
    ("handbag", ["clothing"]),
    ("briefcase", ["clothing"]),
    ("suitcase", ["clothing", "transportation"]),
    ("necklace", ["clothing"]),
    ("bracelet", ["clothing"]),
    ("earring", ["clothing"]),
    ("piercing", ["clothing"]),
    ("makeup", ["clothing"]),
    ("cosmetic", ["clothing"]),
    ("perfume", ["clothing"]),

    # More buildings/places
    ("apartment", ["building"]),
    ("condominium", ["building"]),
    ("mansion", ["building"]),
    ("castle", ["building"]),
    ("palace", ["building"]),
    ("tower", ["building"]),
    ("skyscraper", ["building"]),
    ("stadium", ["building"]),
    ("arena", ["building"]),
    ("gymnasium", ["building"]),
    ("gym", ["building"]),
    ("pool", ["building"]),
    ("museum", ["building"]),
    ("gallery", ["building"]),
    ("theater", ["building", "leisure"]),
    ("cinema", ["building", "leisure"]),
    ("concert hall", ["building", "leisure"]),
    ("auditorium", ["building"]),
    ("clinic", ["building"]),
    ("pharmacy", ["building"]),
    ("drugstore", ["building"]),
    ("supermarket", ["building"]),
    ("department store", ["building"]),
    ("mall", ["building"]),
    ("convenience store", ["building"]),
    ("bookstore", ["building"]),
    ("bakery", ["building", "food"]),
    ("butcher", ["building", "food"]),
    ("factory", ["building", "work"]),
    ("warehouse", ["building"]),
    ("garage", ["building"]),
    ("parking", ["building", "transportation"]),
    ("airport", ["building", "transportation"]),
    ("harbor", ["building", "transportation"]),
    ("port", ["building", "transportation"]),
    ("terminal", ["building", "transportation"]),
    ("bridge", ["building", "transportation"]),
    ("tunnel", ["building", "transportation"]),
    ("prison", ["building"]),
    ("jail", ["building"]),
    ("courthouse", ["building"]),
    ("embassy", ["building"]),
    ("consulate", ["building"]),
    ("city hall", ["building"]),
    ("town hall", ["building"]),
    ("post office", ["building"]),
    ("fire station", ["building"]),
    ("police station", ["building"]),
    ("kindergarten", ["building", "education"]),
    ("nursery", ["building", "education"]),
    ("elementary school", ["building", "education"]),
    ("middle school", ["building", "education"]),
    ("high school", ["building", "education"]),
    ("dormitory", ["building", "education"]),
    ("campus", ["building", "education"]),
    ("laboratory", ["building", "education"]),

    # More transportation
    ("motorcycle", ["transportation"]),
    ("scooter", ["transportation"]),
    ("truck", ["transportation"]),
    ("van", ["transportation"]),
    ("ambulance", ["transportation"]),
    ("fire truck", ["transportation"]),
    ("police car", ["transportation"]),
    ("limousine", ["transportation"]),
    ("helicopter", ["transportation"]),
    ("jet", ["transportation"]),
    ("rocket", ["transportation"]),
    ("spacecraft", ["transportation"]),
    ("ferry", ["transportation"]),
    ("yacht", ["transportation"]),
    ("canoe", ["transportation"]),
    ("kayak", ["transportation"]),
    ("surfboard", ["transportation", "leisure"]),
    ("skateboard", ["transportation", "leisure"]),
    ("roller", ["transportation"]),
    ("wheel", ["transportation"]),
    ("tire", ["transportation"]),
    ("engine", ["transportation"]),
    ("fuel", ["transportation"]),
    ("gasoline", ["transportation"]),
    ("petrol", ["transportation"]),
    ("diesel", ["transportation"]),
    ("traffic", ["transportation"]),
    ("highway", ["transportation"]),
    ("freeway", ["transportation"]),
    ("expressway", ["transportation"]),
    ("intersection", ["transportation"]),
    ("crosswalk", ["transportation"]),
    ("pedestrian", ["transportation", "person"]),
    ("driver", ["transportation", "occupation"]),
    ("passenger", ["transportation", "person"]),
    ("commute", ["transportation", "work"]),
    ("commuter", ["transportation", "person"]),

    # More electronics
    ("laptop", ["electronics"]),
    ("tablet", ["electronics"]),
    ("monitor", ["electronics"]),
    ("screen", ["electronics"]),
    ("keyboard", ["electronics"]),
    ("mouse", ["electronics"]),
    ("printer", ["electronics"]),
    ("scanner", ["electronics"]),
    ("copier", ["electronics"]),
    ("fax", ["electronics"]),
    ("projector", ["electronics"]),
    ("speaker", ["electronics"]),
    ("headphone", ["electronics"]),
    ("earphone", ["electronics"]),
    ("microphone", ["electronics"]),
    ("webcam", ["electronics"]),
    ("router", ["electronics"]),
    ("modem", ["electronics"]),
    ("charger", ["electronics"]),
    ("battery", ["electronics"]),
    ("cable", ["electronics"]),
    ("wire", ["electronics"]),
    ("plug", ["electronics"]),
    ("socket", ["electronics"]),
    ("outlet", ["electronics"]),
    ("switch", ["electronics"]),
    ("remote control", ["electronics"]),
    ("air conditioner", ["electronics"]),
    ("heater", ["electronics"]),
    ("fan", ["electronics"]),
    ("refrigerator", ["electronics"]),
    ("fridge", ["electronics"]),
    ("freezer", ["electronics"]),
    ("microwave", ["electronics"]),
    ("oven", ["electronics"]),
    ("stove", ["electronics"]),
    ("toaster", ["electronics"]),
    ("blender", ["electronics"]),
    ("washer", ["electronics"]),
    ("dryer", ["electronics"]),
    ("vacuum", ["electronics"]),
    ("dishwasher", ["electronics"]),
    ("robot", ["electronics"]),
    ("drone", ["electronics"]),
    ("GPS", ["electronics"]),
    ("app", ["electronics"]),
    ("software", ["electronics"]),
    ("program", ["electronics"]),
    ("website", ["electronics"]),
    ("email", ["electronics", "communication"]),
    ("internet", ["electronics"]),
    ("online", ["electronics"]),
    ("digital", ["electronics"]),
    ("download", ["electronics"]),
    ("upload", ["electronics"]),
    ("streaming", ["electronics"]),
    ("video", ["electronics", "leisure"]),
    ("audio", ["electronics"]),

    # More leisure/entertainment
    ("game", ["leisure"]),
    ("video game", ["leisure", "electronics"]),
    ("board game", ["leisure"]),
    ("card game", ["leisure"]),
    ("puzzle", ["leisure"]),
    ("toy", ["leisure"]),
    ("doll", ["leisure"]),
    ("anime", ["leisure"]),
    ("manga", ["leisure"]),
    ("comic", ["leisure"]),
    ("novel", ["leisure"]),
    ("fiction", ["leisure"]),
    ("drama", ["leisure"]),
    ("comedy", ["leisure"]),
    ("horror", ["leisure"]),
    ("action", ["leisure"]),
    ("romance", ["leisure"]),
    ("documentary", ["leisure"]),
    ("concert", ["leisure"]),
    ("festival", ["leisure"]),
    ("party", ["leisure"]),
    ("celebration", ["leisure"]),
    ("holiday", ["leisure", "time-general"]),
    ("vacation", ["leisure"]),
    ("camping", ["leisure"]),
    ("hiking", ["leisure", "movement"]),
    ("climbing", ["leisure", "movement"]),
    ("swimming", ["leisure", "movement"]),
    ("diving", ["leisure"]),
    ("skiing", ["leisure"]),
    ("snowboarding", ["leisure"]),
    ("skating", ["leisure"]),
    ("surfing", ["leisure"]),
    ("fishing", ["leisure"]),
    ("hunting", ["leisure"]),
    ("golf", ["leisure"]),
    ("tennis", ["leisure"]),
    ("basketball", ["leisure"]),
    ("baseball", ["leisure"]),
    ("football", ["leisure"]),
    ("soccer", ["leisure"]),
    ("volleyball", ["leisure"]),
    ("badminton", ["leisure"]),
    ("boxing", ["leisure"]),
    ("wrestling", ["leisure"]),
    ("martial art", ["leisure"]),
    ("karate", ["leisure"]),
    ("judo", ["leisure"]),
    ("kendo", ["leisure"]),
    ("yoga", ["leisure"]),
    ("meditation", ["leisure"]),
    ("exercise", ["leisure"]),
    ("workout", ["leisure"]),
    ("fitness", ["leisure"]),
    ("jogging", ["leisure", "movement"]),
    ("marathon", ["leisure", "movement"]),
    ("race", ["leisure"]),
    ("competition", ["leisure"]),
    ("tournament", ["leisure"]),
    ("championship", ["leisure"]),
    ("Olympics", ["leisure"]),
    ("photograph", ["leisure"]),
    ("painting", ["leisure"]),
    ("drawing", ["leisure"]),
    ("sculpt", ["leisure"]),
    ("craft", ["leisure"]),
    ("sewing", ["leisure"]),
    ("knitting", ["leisure"]),
    ("garden", ["leisure"]),
    ("gardening", ["leisure"]),
    ("instrument", ["leisure"]),
    ("piano", ["leisure"]),
    ("guitar", ["leisure"]),
    ("violin", ["leisure"]),
    ("drum", ["leisure"]),
    ("flute", ["leisure"]),
    ("trumpet", ["leisure"]),
    ("singing", ["leisure"]),
    ("dancing", ["leisure"]),
    ("dance", ["leisure"]),
    ("ballet", ["leisure"]),
    ("karaoke", ["leisure"]),

    # More occupations
    ("manager", ["occupation", "work"]),
    ("director", ["occupation", "work"]),
    ("president", ["occupation", "work"]),
    ("CEO", ["occupation", "work"]),
    ("executive", ["occupation", "work"]),
    ("secretary", ["occupation", "work"]),
    ("assistant", ["occupation", "work"]),
    ("receptionist", ["occupation", "work"]),
    ("clerk", ["occupation", "work"]),
    ("accountant", ["occupation", "work"]),
    ("banker", ["occupation", "work"]),
    ("consultant", ["occupation", "work"]),
    ("analyst", ["occupation", "work"]),
    ("programmer", ["occupation", "work"]),
    ("developer", ["occupation", "work"]),
    ("designer", ["occupation", "work"]),
    ("architect", ["occupation", "work"]),
    ("scientist", ["occupation", "education"]),
    ("researcher", ["occupation", "education"]),
    ("pharmacist", ["occupation"]),
    ("dentist", ["occupation"]),
    ("surgeon", ["occupation"]),
    ("veterinarian", ["occupation"]),
    ("psychologist", ["occupation"]),
    ("therapist", ["occupation"]),
    ("counselor", ["occupation"]),
    ("firefighter", ["occupation"]),
    ("soldier", ["occupation"]),
    ("military", ["occupation"]),
    ("pilot", ["occupation", "transportation"]),
    ("flight attendant", ["occupation", "transportation"]),
    ("captain", ["occupation", "transportation"]),
    ("sailor", ["occupation", "transportation"]),
    ("mechanic", ["occupation"]),
    ("electrician", ["occupation"]),
    ("plumber", ["occupation"]),
    ("carpenter", ["occupation"]),
    ("construction worker", ["occupation", "work"]),
    ("farmer", ["occupation"]),
    ("fisherman", ["occupation"]),
    ("gardener", ["occupation"]),
    ("chef", ["occupation", "food"]),
    ("baker", ["occupation", "food"]),
    ("waiter", ["occupation", "food"]),
    ("waitress", ["occupation", "food"]),
    ("bartender", ["occupation", "food"]),
    ("barista", ["occupation", "food"]),
    ("hairdresser", ["occupation"]),
    ("barber", ["occupation"]),
    ("beautician", ["occupation"]),
    ("model", ["occupation"]),
    ("photographer", ["occupation", "leisure"]),
    ("journalist", ["occupation", "communication"]),
    ("reporter", ["occupation", "communication"]),
    ("editor", ["occupation", "communication"]),
    ("publisher", ["occupation", "communication"]),
    ("translator", ["occupation", "communication"]),
    ("interpreter", ["occupation", "communication"]),
    ("announcer", ["occupation", "communication"]),
    ("broadcaster", ["occupation", "communication"]),
    ("musician", ["occupation", "leisure"]),
    ("composer", ["occupation", "leisure"]),
    ("conductor", ["occupation", "leisure"]),
    ("actor", ["occupation", "leisure"]),
    ("actress", ["occupation", "leisure"]),
    ("comedian", ["occupation", "leisure"]),
    ("entertainer", ["occupation", "leisure"]),
    ("athlete", ["occupation", "leisure"]),
    ("player", ["occupation", "leisure"]),
    ("coach", ["occupation", "leisure"]),
    ("referee", ["occupation", "leisure"]),
    ("judge", ["occupation"]),
    ("politician", ["occupation"]),
    ("diplomat", ["occupation"]),
    ("minister", ["occupation"]),
    ("mayor", ["occupation"]),
    ("governor", ["occupation"]),
    ("priest", ["occupation"]),
    ("monk", ["occupation"]),
    ("nun", ["occupation"]),

    # More work/business
    ("salary", ["work"]),
    ("wage", ["work"]),
    ("income", ["work"]),
    ("bonus", ["work"]),
    ("pension", ["work"]),
    ("retirement", ["work"]),
    ("promotion", ["work"]),
    ("demotion", ["work"]),
    ("transfer", ["work"]),
    ("resignation", ["work"]),
    ("termination", ["work"]),
    ("layoff", ["work"]),
    ("interview", ["work"]),
    ("resume", ["work"]),
    ("contract", ["work"]),
    ("agreement", ["work"]),
    ("negotiation", ["work"]),
    ("deal", ["work"]),
    ("client", ["work"]),
    ("customer", ["work"]),
    ("supplier", ["work"]),
    ("vendor", ["work"]),
    ("partner", ["work"]),
    ("competitor", ["work"]),
    ("market", ["work"]),
    ("industry", ["work"]),
    ("sector", ["work"]),
    ("profit", ["work"]),
    ("loss", ["work"]),
    ("revenue", ["work"]),
    ("expense", ["work"]),
    ("budget", ["work"]),
    ("investment", ["work"]),
    ("stock", ["work"]),
    ("share", ["work"]),
    ("dividend", ["work"]),
    ("loan", ["work"]),
    ("debt", ["work"]),
    ("credit", ["work"]),
    ("tax", ["work"]),
    ("insurance", ["work"]),

    # More education
    ("textbook", ["education"]),
    ("curriculum", ["education"]),
    ("syllabus", ["education"]),
    ("semester", ["education", "time-general"]),
    ("quarter", ["education", "time-general"]),
    ("grade", ["education"]),
    ("score", ["education"]),
    ("diploma", ["education"]),
    ("degree", ["education"]),
    ("certificate", ["education"]),
    ("graduation", ["education"]),
    ("commencement", ["education"]),
    ("enrollment", ["education"]),
    ("admission", ["education"]),
    ("tuition", ["education"]),
    ("scholarship", ["education"]),
    ("fellowship", ["education"]),
    ("research", ["education"]),
    ("thesis", ["education"]),
    ("dissertation", ["education"]),
    ("paper", ["education", "communication"]),
    ("essay", ["education", "communication"]),
    ("report", ["education", "communication"]),
    ("presentation", ["education", "communication"]),
    ("lecture", ["education"]),
    ("seminar", ["education"]),
    ("workshop", ["education"]),
    ("tutorial", ["education"]),
    ("major", ["education"]),
    ("minor", ["education"]),
    ("subject", ["education"]),
    ("mathematics", ["education"]),
    ("science", ["education"]),
    ("physics", ["education"]),
    ("chemistry", ["education"]),
    ("biology", ["education"]),
    ("history", ["education"]),
    ("geography", ["education", "geography"]),
    ("literature", ["education"]),
    ("philosophy", ["education"]),
    ("psychology", ["education"]),
    ("sociology", ["education"]),
    ("economics", ["education", "work"]),
    ("political", ["education"]),
    ("law", ["education"]),
    ("medicine", ["education"]),
    ("engineering", ["education"]),

    # More geography/nature
    ("continent", ["geography"]),
    ("country", ["geography"]),
    ("nation", ["geography"]),
    ("state", ["geography"]),
    ("province", ["geography"]),
    ("region", ["geography"]),
    ("area", ["geography"]),
    ("district", ["geography"]),
    ("city", ["geography"]),
    ("town", ["geography"]),
    ("village", ["geography"]),
    ("neighborhood", ["geography"]),
    ("peninsula", ["geography"]),
    ("cape", ["geography"]),
    ("gulf", ["geography"]),
    ("bay", ["geography"]),
    ("strait", ["geography"]),
    ("channel", ["geography"]),
    ("cliff", ["geography"]),
    ("cave", ["geography"]),
    ("crater", ["geography"]),
    ("volcano", ["geography"]),
    ("earthquake", ["geography", "weather"]),
    ("tsunami", ["geography", "weather"]),
    ("flood", ["weather"]),
    ("drought", ["weather"]),
    ("tornado", ["weather"]),
    ("blizzard", ["weather"]),
    ("hail", ["weather"]),
    ("frost", ["weather"]),
    ("dew", ["weather"]),
    ("rainbow", ["weather"]),
    ("sky", ["weather"]),
    ("atmosphere", ["weather"]),
    ("climate", ["weather"]),
    ("temperature", ["weather"]),
    ("humidity", ["weather"]),

    # More communication
    ("language", ["communication"]),
    ("word", ["communication"]),
    ("sentence", ["communication"]),
    ("phrase", ["communication"]),
    ("paragraph", ["communication"]),
    ("chapter", ["communication"]),
    ("page", ["communication"]),
    ("book", ["communication", "tool"]),
    ("magazine", ["communication"]),
    ("newspaper", ["communication"]),
    ("article", ["communication"]),
    ("blog", ["communication"]),
    ("post", ["communication"]),
    ("comment", ["communication"]),
    ("message", ["communication"]),
    ("letter", ["communication"]),
    ("mail", ["communication"]),
    ("parcel", ["communication"]),
    ("package", ["communication"]),
    ("delivery", ["communication"]),
    ("announcement", ["communication"]),
    ("notice", ["communication"]),
    ("advertisement", ["communication"]),
    ("commercial", ["communication"]),
    ("sign", ["communication"]),
    ("symbol", ["communication"]),
    ("signal", ["communication"]),
    ("gesture", ["communication"]),
    ("expression", ["communication"]),
    ("tone", ["communication"]),
    ("accent", ["communication"]),
    ("dialect", ["communication"]),
    ("pronunciation", ["communication"]),
    ("spelling", ["communication"]),
    ("grammar", ["communication"]),
    ("vocabulary", ["communication"]),
    ("translation", ["communication"]),
    ("interpretation", ["communication"]),

    # Tools and materials
    ("hammer", ["tool"]),
    ("screwdriver", ["tool"]),
    ("wrench", ["tool"]),
    ("pliers", ["tool"]),
    ("saw", ["tool"]),
    ("drill", ["tool"]),
    ("nail", ["tool"]),
    ("screw", ["tool"]),
    ("bolt", ["tool"]),
    ("nut", ["tool"]),
    ("rope", ["tool"]),
    ("chain", ["tool"]),
    ("tape", ["tool"]),
    ("glue", ["tool"]),
    ("paint", ["tool"]),
    ("brush", ["tool"]),
    ("ruler", ["tool"]),
    ("meter", ["tool"]),
    ("scale", ["tool"]),
    ("thermometer", ["tool"]),
    ("compass", ["tool"]),
    ("calculator", ["tool", "electronics"]),
    ("calendar", ["tool", "time-general"]),
    ("clock", ["tool", "time-general"]),
    ("watch", ["tool", "clothing", "time-general"]),
    ("alarm", ["tool"]),
    ("bell", ["tool"]),
    ("whistle", ["tool"]),
    ("flashlight", ["tool"]),
    ("lantern", ["tool"]),
    ("candle", ["tool"]),
    ("match", ["tool"]),
    ("lighter", ["tool"]),
    ("mirror", ["tool"]),
    ("lens", ["tool"]),
    ("telescope", ["tool"]),
    ("microscope", ["tool"]),
    ("binocular", ["tool"]),

    # Furniture
    ("couch", ["furniture"]),
    ("armchair", ["furniture"]),
    ("stool", ["furniture"]),
    ("bench", ["furniture"]),
    ("cabinet", ["furniture"]),
    ("drawer", ["furniture"]),
    ("closet", ["furniture"]),
    ("wardrobe", ["furniture"]),
    ("bookshelf", ["furniture"]),
    ("counter", ["furniture"]),
    ("sink", ["furniture"]),
    ("bathtub", ["furniture"]),
    ("shower", ["furniture"]),
    ("toilet", ["furniture"]),
    ("curtain", ["furniture"]),
    ("blind", ["furniture"]),
    ("carpet", ["furniture"]),
    ("rug", ["furniture"]),
    ("mat", ["furniture"]),
    ("pillow", ["furniture"]),
    ("blanket", ["furniture"]),
    ("sheet", ["furniture"]),
    ("mattress", ["furniture"]),
    ("futon", ["furniture"]),
    ("lamp", ["furniture"]),
    ("chandelier", ["furniture"]),

    # More body/health
    ("health", ["body-part"]),
    ("illness", ["body-part"]),
    ("disease", ["body-part"]),
    ("symptom", ["body-part"]),
    ("pain", ["body-part", "emotion"]),
    ("ache", ["body-part"]),
    ("fever", ["body-part"]),
    ("cough", ["body-part"]),
    ("cold", ["body-part"]),
    ("flu", ["body-part"]),
    ("allergy", ["body-part"]),
    ("infection", ["body-part"]),
    ("injury", ["body-part"]),
    ("wound", ["body-part"]),
    ("scar", ["body-part"]),
    ("bruise", ["body-part"]),
    ("burn", ["body-part"]),
    ("fracture", ["body-part"]),
    ("surgery", ["body-part"]),
    ("operation", ["body-part"]),
    ("treatment", ["body-part"]),
    ("therapy", ["body-part"]),
    ("medicine", ["body-part"]),
    ("drug", ["body-part"]),
    ("pill", ["body-part"]),
    ("injection", ["body-part"]),
    ("vaccine", ["body-part"]),
    ("prescription", ["body-part"]),
    ("diagnosis", ["body-part"]),
    ("checkup", ["body-part"]),
    ("examination", ["body-part"]),

    # Time-related
    ("date", ["time-general"]),
    ("calendar", ["time-general"]),
    ("schedule", ["time-general"]),
    ("appointment", ["time-general"]),
    ("deadline", ["time-general"]),
    ("anniversary", ["time-general"]),
    ("birthday", ["time-general"]),
    ("century", ["time-general"]),
    ("decade", ["time-general"]),
    ("generation", ["time-general"]),
    ("era", ["time-general"]),
    ("period", ["time-general"]),
    ("ancient", ["time-general"]),
    ("modern", ["time-general"]),
    ("contemporary", ["time-general"]),
    ("recent", ["time-general"]),
    ("current", ["time-general"]),
    ("previous", ["time-general"]),
    ("next", ["time-general"]),
    ("weekly", ["time-general"]),
    ("monthly", ["time-general"]),
    ("yearly", ["time-general"]),
    ("annual", ["time-general"]),
    ("daily", ["time-general"]),
    ("hourly", ["time-general"]),

    # More animals
    ("reptile", ["animal-general"]),
    ("amphibian", ["animal-general"]),
    ("snake", ["animal-general"]),
    ("lizard", ["animal-general"]),
    ("turtle", ["animal-general"]),
    ("frog", ["animal-general"]),
    ("toad", ["animal-general"]),
    ("crocodile", ["animal-general"]),
    ("alligator", ["animal-general"]),
    ("dinosaur", ["animal-general"]),
    ("shellfish", ["animal-fish"]),
    ("clam", ["animal-fish"]),
    ("oyster", ["animal-fish"]),
    ("mussel", ["animal-fish"]),
    ("lobster", ["animal-fish"]),
    ("snail", ["animal-insect"]),
    ("slug", ["animal-insect"]),
    ("worm", ["animal-insect"]),
    ("caterpillar", ["animal-insect"]),
    ("moth", ["animal-insect"]),
    ("cockroach", ["animal-insect"]),
    ("grasshopper", ["animal-insect"]),
    ("cricket", ["animal-insect"]),
    ("firefly", ["animal-insect"]),
    ("ladybug", ["animal-insect"]),
    ("penguin", ["animal-bird"]),
    ("flamingo", ["animal-bird"]),
    ("peacock", ["animal-bird"]),
    ("parrot", ["animal-bird"]),
    ("seagull", ["animal-bird"]),
    ("heron", ["animal-bird"]),
    ("woodpecker", ["animal-bird"]),
    ("robin", ["animal-bird"]),
    ("canary", ["animal-bird"]),
    ("giraffe", ["animal-mammal"]),
    ("zebra", ["animal-mammal"]),
    ("hippo", ["animal-mammal"]),
    ("rhino", ["animal-mammal"]),
    ("gorilla", ["animal-mammal"]),
    ("chimpanzee", ["animal-mammal"]),
    ("koala", ["animal-mammal"]),
    ("kangaroo", ["animal-mammal"]),
    ("panda", ["animal-mammal"]),
    ("polar bear", ["animal-mammal"]),
    ("seal", ["animal-mammal"]),
    ("otter", ["animal-mammal"]),
    ("beaver", ["animal-mammal"]),
    ("squirrel", ["animal-mammal"]),
    ("hamster", ["animal-mammal"]),
    ("guinea pig", ["animal-mammal"]),
    ("hedgehog", ["animal-mammal"]),
    ("bat", ["animal-mammal"]),
    ("camel", ["animal-mammal"]),
    ("donkey", ["animal-mammal"]),
    ("mule", ["animal-mammal"]),
    ("buffalo", ["animal-mammal"]),
    ("bison", ["animal-mammal"]),
    ("moose", ["animal-mammal"]),
    ("reindeer", ["animal-mammal"]),
    ("antelope", ["animal-mammal"]),
    ("boar", ["animal-mammal"]),
    ("raccoon", ["animal-mammal"]),
    ("skunk", ["animal-mammal"]),
    ("weasel", ["animal-mammal"]),
    ("mink", ["animal-mammal"]),
    ("badger", ["animal-mammal"]),
    ("porcupine", ["animal-mammal"]),
    ("hyena", ["animal-mammal"]),
    ("jaguar", ["animal-mammal"]),
    ("leopard", ["animal-mammal"]),
    ("cheetah", ["animal-mammal"]),
    ("panther", ["animal-mammal"]),
    ("cougar", ["animal-mammal"]),

    # Emotions and states
    ("anxiety", ["emotion"]),
    ("depression", ["emotion"]),
    ("stress", ["emotion"]),
    ("frustration", ["emotion"]),
    ("disappointment", ["emotion"]),
    ("regret", ["emotion"]),
    ("guilt", ["emotion"]),
    ("shame", ["emotion"]),
    ("pride", ["emotion"]),
    ("confidence", ["emotion"]),
    ("courage", ["emotion"]),
    ("hope", ["emotion"]),
    ("despair", ["emotion"]),
    ("jealousy", ["emotion"]),
    ("envy", ["emotion"]),
    ("sympathy", ["emotion"]),
    ("empathy", ["emotion"]),
    ("compassion", ["emotion"]),
    ("gratitude", ["emotion"]),
    ("appreciation", ["emotion"]),
    ("admiration", ["emotion"]),
    ("respect", ["emotion"]),
    ("disgust", ["emotion"]),
    ("contempt", ["emotion"]),
    ("boredom", ["emotion"]),
    ("curiosity", ["emotion"]),
    ("excitement", ["emotion"]),
    ("enthusiasm", ["emotion"]),
    ("passion", ["emotion"]),
    ("desire", ["emotion"]),
    ("longing", ["emotion"]),
    ("nostalgia", ["emotion"]),
    ("satisfaction", ["emotion"]),
    ("contentment", ["emotion"]),
    ("relief", ["emotion"]),
    ("comfort", ["emotion"]),
    ("peace", ["emotion"]),
    ("calm", ["emotion"]),
    ("serenity", ["emotion"]),
    ("tension", ["emotion"]),
    ("nervousness", ["emotion"]),
    ("embarrassment", ["emotion"]),
    ("confusion", ["emotion"]),
    ("bewilderment", ["emotion"]),
    ("amazement", ["emotion"]),
    ("wonder", ["emotion"]),
    ("awe", ["emotion"]),
]

# POS-based fallback categories
POS_FALLBACK_TAGS = {
    # Verbs get "action" as a fallback
    "verb-godan": ["action"],
    "verb-ichidan": ["action"],
    "verb-suru": ["action"],
    "verb-kuru": ["action"],
    "verb-irregular": ["action"],
    # Adjectives get "descriptive"
    "adjective-i": ["descriptive"],
    "adjective-na": ["descriptive"],
    "adjective-no": ["descriptive"],
    "adjective-taru": ["descriptive"],
    # Adverbs get "descriptive"
    "adverb": ["descriptive"],
    # Conjunctions and particles are grammatical
    "conjunction": ["grammatical"],
    "particle": ["grammatical"],
    # Onomatopoeia
    "onomatopoeia": ["onomatopoeia"],
    # Interjections
    "interjection": ["expression"],
    # Expressions
    "expression": ["expression"],
}


def strip_furigana(text: str) -> str:
    """Remove furigana markup from text."""
    return re.sub(r"\{([^|]+)\|[^}]+\}", r"\1", text)


def get_all_text(entry: dict) -> str:
    """Get all searchable text from an entry (gloss + definitions)."""
    texts = []

    gloss = entry.get("gloss", "")
    if gloss:
        texts.append(gloss)

    for defn in entry.get("definitions", []):
        if defn.get("gloss"):
            texts.append(defn["gloss"])

    return " ".join(texts).lower()


def get_semantic_tags(entry: dict) -> list[str]:
    """Get semantic tags for an entry."""
    tags = set()
    all_text = get_all_text(entry)
    gloss = entry.get("gloss", "").lower()

    # Check gloss-contains rules
    for keyword, tag_list in GLOSS_CONTAINS_RULES:
        if keyword.lower() in all_text:
            tags.update(tag_list)

    # If we found specific tags, return them
    if tags:
        return sorted(list(tags))

    # Otherwise, use POS-based fallback
    pos_list = entry.get("metadata", {}).get("tags", {}).get("pos", [])
    for pos in pos_list:
        if pos in POS_FALLBACK_TAGS:
            tags.update(POS_FALLBACK_TAGS[pos])

    # If still no tags, use "general" as ultimate fallback for nouns
    if not tags and "noun" in pos_list:
        tags.add("general")

    return sorted(list(tags))


def migrate_all_entries(
    project_root: Path,
    dry_run: bool = True,
    verbose: bool = False
) -> dict:
    """Add semantic tags to entries without them."""
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
            continue

        # Get tags
        semantic_tags = get_semantic_tags(entry)

        if not semantic_tags:
            stats["no_match"] += 1
            if verbose:
                hw = entry.get("headword", "")
                gl = entry.get("gloss", "")
                print(f"  No match: {file_path.name} - {hw} ({gl})")
            continue

        stats["tagged"] += 1
        for tag in semantic_tags:
            stats["tag_counts"][tag] += 1

        if verbose or dry_run:
            rel_path = file_path.relative_to(project_root)
            hw = entry.get("headword", "")
            gl = entry.get("gloss", "")[:40]
            print(f"  {rel_path}: {hw} ({gl}...) -> {semantic_tags}")

        # Write if not dry run
        if not dry_run:
            # Initialize metadata.tags if needed
            if "metadata" not in entry:
                entry["metadata"] = {}
            if "tags" not in entry["metadata"]:
                entry["metadata"]["tags"] = {}

            entry["metadata"]["tags"]["semantic"] = semantic_tags
            entry["metadata"]["modified"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(entry, f, ensure_ascii=False, indent=2)

    return stats


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Expand semantic tags to untagged entries"
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
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output"
    )
    args = parser.parse_args()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    if not (args.dry_run or args.apply):
        print("Error: Must specify --dry-run or --apply")
        parser.print_help()
        return 1

    # Migration mode
    mode = "DRY RUN" if args.dry_run else "APPLY"
    print(f"Expanded Semantic Tag Migration ({mode})")
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
        print(f"\nTag distribution (top 30):")
        for tag, count in stats["tag_counts"].most_common(30):
            print(f"  {tag}: {count}")

    coverage = (stats['already_tagged'] + stats['tagged']) / stats['total'] * 100 if stats['total'] > 0 else 0
    print(f"\nSemantic coverage: {coverage:.1f}%")

    if args.dry_run and stats["tagged"] > 0:
        print(f"\nTo apply these changes, run: python3 {sys.argv[0]} --apply")

    return 0


if __name__ == "__main__":
    sys.exit(main())
