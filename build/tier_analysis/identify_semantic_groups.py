#!/usr/bin/env python3
"""
Identify semantic groups in the dictionary for vocabulary tier analysis.
"""

import json
import re
from collections import defaultdict

# Load all entries
with open('build/tier_analysis/all_entries.json') as f:
    entries = json.load(f)

# Create lookup by reading and headword
by_reading = {e['reading']: e for e in entries}
by_headword = {e['headword']: e for e in entries}

def find_entries(patterns, by='reading'):
    """Find entries matching given patterns."""
    found = []
    lookup = by_reading if by == 'reading' else by_headword
    for pattern in patterns:
        if pattern in lookup:
            found.append(lookup[pattern])
    return found

def count_tiers(entries_list):
    """Count tier distribution for a list of entries."""
    tiers = defaultdict(int)
    for e in entries_list:
        tier = e['tier'] or 'null'
        tiers[tier] += 1
    return dict(tiers)

# Define semantic groups

semantic_groups = {}

# 1. Days of week
days_readings = ['げつようび', 'かようび', 'すいようび', 'もくようび', 'きんようび', 'どようび', 'にちようび']
days_headwords = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
days = find_entries(days_readings) or find_entries(days_headwords, by='headword')
if days:
    semantic_groups['days_of_week'] = {
        'description': 'Days of the week (Monday-Sunday)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in days],
        'entry_ids': [e['id'] for e in days],
        'current_tiers': count_tiers(days),
        'count': len(days),
        'expected': 7
    }

# 2. Months
months_readings = ['いちがつ', 'にがつ', 'さんがつ', 'しがつ', 'ごがつ', 'ろくがつ',
                   'しちがつ', 'はちがつ', 'くがつ', 'じゅうがつ', 'じゅういちがつ', 'じゅうにがつ']
months_headwords = ['一月', '二月', '三月', '四月', '五月', '六月',
                    '七月', '八月', '九月', '十月', '十一月', '十二月']
months = find_entries(months_readings) or find_entries(months_headwords, by='headword')
if months:
    semantic_groups['months'] = {
        'description': 'Months of the year (January-December)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in months],
        'entry_ids': [e['id'] for e in months],
        'current_tiers': count_tiers(months),
        'count': len(months),
        'expected': 12
    }

# 3. Numbers 1-10
numbers_readings = ['いち', 'に', 'さん', 'よん', 'し', 'ご', 'ろく', 'なな', 'しち', 'はち', 'きゅう', 'く', 'じゅう', 'ぜろ', 'れい']
numbers_headwords = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '零']
numbers = find_entries(numbers_headwords, by='headword')
if numbers:
    semantic_groups['numbers_basic'] = {
        'description': 'Basic numbers (0-10)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in numbers],
        'entry_ids': [e['id'] for e in numbers],
        'current_tiers': count_tiers(numbers),
        'count': len(numbers),
        'expected': 11
    }

# 4. Numbers by tens (20-100)
tens_headwords = ['二十', '三十', '四十', '五十', '六十', '七十', '八十', '九十', '百']
tens = find_entries(tens_headwords, by='headword')
if tens:
    semantic_groups['numbers_tens'] = {
        'description': 'Numbers by tens (20-100)',
        'target_tier': 'core',
        'entries': [e['reading'] for e in tens],
        'entry_ids': [e['id'] for e in tens],
        'current_tiers': count_tiers(tens),
        'count': len(tens),
        'expected': 9
    }

# 5. Large numbers
large_nums = ['千', '万', '億']
large = find_entries(large_nums, by='headword')
if large:
    semantic_groups['numbers_large'] = {
        'description': 'Large number units (thousand, ten-thousand, hundred-million)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in large],
        'entry_ids': [e['id'] for e in large],
        'current_tiers': count_tiers(large),
        'count': len(large),
        'expected': 3
    }

# 6. Counter: つ series
tsu_readings = ['ひとつ', 'ふたつ', 'みっつ', 'よっつ', 'いつつ', 'むっつ', 'ななつ', 'やっつ', 'ここのつ', 'とお']
tsu = find_entries(tsu_readings)
if tsu:
    semantic_groups['counter_tsu'] = {
        'description': 'Generic counter つ series (1-10)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in tsu],
        'entry_ids': [e['id'] for e in tsu],
        'current_tiers': count_tiers(tsu),
        'count': len(tsu),
        'expected': 10
    }

# 7. Other counters
counter_patterns = ['人', '個', '本', '枚', '冊', '匹', '頭', '台', '杯', '回', '度', '階', '番', '歳', '才', '年', '月', '日', '時', '分', '秒', '週', '円', '件', '軒', '足']
counters = []
for e in entries:
    if e['pos'] == 'counter':
        counters.append(e)
if counters:
    semantic_groups['counters_general'] = {
        'description': 'Counter words (人, 個, 本, 枚, etc.)',
        'target_tier': 'mixed (basic for common, core/general for specialized)',
        'entries': [e['reading'] for e in counters],
        'entry_ids': [e['id'] for e in counters],
        'current_tiers': count_tiers(counters),
        'count': len(counters),
        'expected': 'varies'
    }

# 8. Directions (relative)
direction_headwords = ['上', '下', '右', '左', '前', '後ろ', '中', '外', '横', '隣', '奥', '手前']
direction_readings = ['うえ', 'した', 'みぎ', 'ひだり', 'まえ', 'うしろ', 'なか', 'そと', 'よこ', 'となり', 'おく', 'てまえ']
directions = find_entries(direction_readings)
if directions:
    semantic_groups['directions_relative'] = {
        'description': 'Relative directions (up, down, left, right, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in directions],
        'entry_ids': [e['id'] for e in directions],
        'current_tiers': count_tiers(directions),
        'count': len(directions),
        'expected': 12
    }

# 9. Cardinal directions
cardinal_headwords = ['北', '南', '東', '西']
cardinal_readings = ['きた', 'みなみ', 'ひがし', 'にし']
cardinals = find_entries(cardinal_readings)
if cardinals:
    semantic_groups['directions_cardinal'] = {
        'description': 'Cardinal directions (north, south, east, west)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in cardinals],
        'entry_ids': [e['id'] for e in cardinals],
        'current_tiers': count_tiers(cardinals),
        'count': len(cardinals),
        'expected': 4
    }

# 10. Body parts
body_readings = ['あたま', 'かお', 'め', 'みみ', 'くち', 'はな', 'て', 'あし', 'ゆび', 'かみ',
                'くび', 'かた', 'うで', 'むね', 'せなか', 'おなか', 'こし', 'ひざ', 'は', 'した']
body = find_entries(body_readings)
if body:
    semantic_groups['body_parts'] = {
        'description': 'Body parts (head, face, eyes, ears, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in body],
        'entry_ids': [e['id'] for e in body],
        'current_tiers': count_tiers(body),
        'count': len(body),
        'expected': 20
    }

# 11. Family terms (plain)
family_plain = ['ちち', 'はは', 'あに', 'あね', 'おとうと', 'いもうと', 'そふ', 'そぼ', 'おじ', 'おば',
                'むすこ', 'むすめ', 'まご', 'おっと', 'つま', 'りょうしん', 'きょうだい', 'こども', 'おや', 'かぞく']
family_p = find_entries(family_plain)
if family_p:
    semantic_groups['family_plain'] = {
        'description': 'Family terms (plain/humble forms)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in family_p],
        'entry_ids': [e['id'] for e in family_p],
        'current_tiers': count_tiers(family_p),
        'count': len(family_p),
        'expected': 20
    }

# 12. Family terms (honorific)
family_hon = ['おとうさん', 'おかあさん', 'おにいさん', 'おねえさん', 'おじいさん', 'おばあさん', 'おじさん', 'おばさん']
family_h = find_entries(family_hon)
if family_h:
    semantic_groups['family_honorific'] = {
        'description': 'Family terms (honorific forms)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in family_h],
        'entry_ids': [e['id'] for e in family_h],
        'current_tiers': count_tiers(family_h),
        'count': len(family_h),
        'expected': 8
    }

# 13. Colors
color_readings = ['あか', 'あお', 'しろ', 'くろ', 'きいろ', 'みどり', 'ちゃいろ', 'むらさき', 'おれんじ', 'ぴんく', 'はいいろ', 'きん', 'ぎん']
colors = find_entries(color_readings)
if colors:
    semantic_groups['colors'] = {
        'description': 'Color words (red, blue, white, black, etc.)',
        'target_tier': 'basic (core 5), core (others)',
        'entries': [e['reading'] for e in colors],
        'entry_ids': [e['id'] for e in colors],
        'current_tiers': count_tiers(colors),
        'count': len(colors),
        'expected': 13
    }

# 14. Question words
question_readings = ['なに', 'なん', 'だれ', 'どこ', 'いつ', 'なぜ', 'どう', 'どれ', 'どの', 'どちら', 'いくつ', 'いくら', 'どんな']
questions = find_entries(question_readings)
if questions:
    semantic_groups['question_words'] = {
        'description': 'Question words (what, who, where, when, why, how, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in questions],
        'entry_ids': [e['id'] for e in questions],
        'current_tiers': count_tiers(questions),
        'count': len(questions),
        'expected': 13
    }

# 15. Demonstratives - ko-so-a-do series
demo_readings = ['これ', 'それ', 'あれ', 'どれ', 'この', 'その', 'あの', 'どの',
                 'ここ', 'そこ', 'あそこ', 'どこ', 'こちら', 'そちら', 'あちら', 'どちら',
                 'こう', 'そう', 'ああ', 'どう', 'こんな', 'そんな', 'あんな', 'どんな']
demos = find_entries(demo_readings)
if demos:
    semantic_groups['demonstratives'] = {
        'description': 'Ko-so-a-do demonstrative series',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in demos],
        'entry_ids': [e['id'] for e in demos],
        'current_tiers': count_tiers(demos),
        'count': len(demos),
        'expected': 24
    }

# 16. Pronouns
pronoun_readings = ['わたし', 'ぼく', 'おれ', 'あなた', 'かれ', 'かのじょ', 'わたしたち', 'われわれ',
                    'あなたたち', 'かれら', 'じぶん', 'みんな', 'だれか', 'だれも', 'なにか', 'なにも']
pronouns = find_entries(pronoun_readings)
if pronouns:
    semantic_groups['pronouns'] = {
        'description': 'Personal pronouns and indefinite pronouns',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in pronouns],
        'entry_ids': [e['id'] for e in pronouns],
        'current_tiers': count_tiers(pronouns),
        'count': len(pronouns),
        'expected': 16
    }

# 17. Seasons
season_readings = ['はる', 'なつ', 'あき', 'ふゆ']
seasons = find_entries(season_readings)
if seasons:
    semantic_groups['seasons'] = {
        'description': 'Seasons (spring, summer, autumn, winter)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in seasons],
        'entry_ids': [e['id'] for e in seasons],
        'current_tiers': count_tiers(seasons),
        'count': len(seasons),
        'expected': 4
    }

# 18. Basic existence verbs
exist_readings = ['いる', 'ある']
existence = find_entries(exist_readings)
if existence:
    semantic_groups['verbs_existence'] = {
        'description': 'Existence verbs (いる, ある)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in existence],
        'entry_ids': [e['id'] for e in existence],
        'current_tiers': count_tiers(existence),
        'count': len(existence),
        'expected': 2
    }

# 19. Basic movement verbs
movement_readings = ['いく', 'くる', 'かえる', 'あるく', 'はしる', 'とまる', 'はいる', 'でる', 'のる', 'おりる', 'わたる', 'とおる']
movement = find_entries(movement_readings)
if movement:
    semantic_groups['verbs_movement'] = {
        'description': 'Basic movement verbs (go, come, return, walk, run, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in movement],
        'entry_ids': [e['id'] for e in movement],
        'current_tiers': count_tiers(movement),
        'count': len(movement),
        'expected': 12
    }

# 20. Basic daily verbs
daily_readings = ['たべる', 'のむ', 'ねる', 'おきる', 'あらう', 'きる', 'ぬぐ', 'つくる', 'みる', 'きく', 'かく']
daily = find_entries(daily_readings)
if daily:
    semantic_groups['verbs_daily'] = {
        'description': 'Basic daily action verbs (eat, drink, sleep, wake up, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in daily],
        'entry_ids': [e['id'] for e in daily],
        'current_tiers': count_tiers(daily),
        'count': len(daily),
        'expected': 11
    }

# 21. Basic communication verbs
comm_readings = ['いう', 'はなす', 'きく', 'よむ', 'かく', 'おしえる', 'ならう', 'こたえる', 'きく', 'たずねる', 'よぶ']
comm = find_entries(comm_readings)
if comm:
    semantic_groups['verbs_communication'] = {
        'description': 'Basic communication verbs (say, speak, listen, read, write, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in comm],
        'entry_ids': [e['id'] for e in comm],
        'current_tiers': count_tiers(comm),
        'count': len(comm),
        'expected': 10
    }

# 22. Time periods
time_period_readings = ['あさ', 'ひる', 'ゆうがた', 'よる', 'よなか', 'ごぜん', 'ごご', 'まいにち', 'まいあさ', 'まいばん']
time_periods = find_entries(time_period_readings)
if time_periods:
    semantic_groups['time_periods'] = {
        'description': 'Time of day (morning, noon, evening, night, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in time_periods],
        'entry_ids': [e['id'] for e in time_periods],
        'current_tiers': count_tiers(time_periods),
        'count': len(time_periods),
        'expected': 10
    }

# 23. Relative time
relative_time_readings = ['きょう', 'あした', 'あす', 'きのう', 'おととい', 'あさって', 'こんしゅう', 'らいしゅう', 'せんしゅう',
                          'こんげつ', 'らいげつ', 'せんげつ', 'ことし', 'らいねん', 'きょねん', 'いま', 'むかし', 'みらい', 'さいきん']
relative = find_entries(relative_time_readings)
if relative:
    semantic_groups['time_relative'] = {
        'description': 'Relative time expressions (today, tomorrow, yesterday, this week, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in relative],
        'entry_ids': [e['id'] for e in relative],
        'current_tiers': count_tiers(relative),
        'count': len(relative),
        'expected': 19
    }

# 24. Particles (all particles in the dictionary)
particles = [e for e in entries if e['pos'] == 'particle']
if particles:
    semantic_groups['particles'] = {
        'description': 'All particles (は, が, を, に, で, etc.)',
        'target_tier': 'basic (core particles), core/general (specialized)',
        'entries': [e['reading'] for e in particles],
        'entry_ids': [e['id'] for e in particles],
        'current_tiers': count_tiers(particles),
        'count': len(particles),
        'expected': 'varies'
    }

# 25. Basic adjectives - い adjectives
i_adj_basic = ['いい', 'わるい', 'おおきい', 'ちいさい', 'あたらしい', 'ふるい', 'たかい', 'やすい', 'ひくい',
               'ながい', 'みじかい', 'おおい', 'すくない', 'あつい', 'さむい', 'つめたい', 'あたたかい',
               'おもしろい', 'つまらない', 'むずかしい', 'やさしい', 'うれしい', 'かなしい', 'たのしい',
               'いそがしい', 'ひまな', 'はやい', 'おそい', 'つよい', 'よわい']
i_adj = find_entries(i_adj_basic)
if i_adj:
    semantic_groups['adjectives_i_basic'] = {
        'description': 'Basic i-adjectives (good, bad, big, small, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in i_adj],
        'entry_ids': [e['id'] for e in i_adj],
        'current_tiers': count_tiers(i_adj),
        'count': len(i_adj),
        'expected': 30
    }

# 26. Basic na-adjectives
na_adj_basic = ['げんきな', 'しずかな', 'にぎやかな', 'きれいな', 'ゆうめいな', 'べんりな', 'ふべんな',
                'かんたんな', 'ふくざつな', 'だいじな', 'たいせつな', 'だめな', 'すきな', 'きらいな', 'じょうずな', 'へたな']
na_adj = find_entries(na_adj_basic)
# Also try without な
na_adj_base = ['げんき', 'しずか', 'にぎやか', 'きれい', 'ゆうめい', 'べんり', 'ふべん',
               'かんたん', 'ふくざつ', 'だいじ', 'たいせつ', 'だめ', 'すき', 'きらい', 'じょうず', 'へた']
na_adj2 = find_entries(na_adj_base)
na_adj_combined = list({e['id']: e for e in (na_adj + na_adj2)}.values())
if na_adj_combined:
    semantic_groups['adjectives_na_basic'] = {
        'description': 'Basic na-adjectives (healthy, quiet, famous, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in na_adj_combined],
        'entry_ids': [e['id'] for e in na_adj_combined],
        'current_tiers': count_tiers(na_adj_combined),
        'count': len(na_adj_combined),
        'expected': 16
    }

# 27. Basic adverbs
adverb_readings = ['とても', 'すこし', 'ちょっと', 'たくさん', 'もう', 'まだ', 'いつも', 'よく', 'ときどき', 'あまり',
                   'ぜんぜん', 'たぶん', 'きっと', 'もちろん', 'ぜひ', 'やっと', 'すぐ', 'ゆっくり', 'だんだん', 'ずっと']
adverbs = find_entries(adverb_readings)
if adverbs:
    semantic_groups['adverbs_basic'] = {
        'description': 'Basic adverbs (very, little, already, still, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in adverbs],
        'entry_ids': [e['id'] for e in adverbs],
        'current_tiers': count_tiers(adverbs),
        'count': len(adverbs),
        'expected': 20
    }

# 28. Common nouns - places
place_readings = ['いえ', 'うち', 'へや', 'まち', 'みせ', 'えき', 'くうこう', 'がっこう', 'だいがく', 'びょういん',
                  'ぎんこう', 'ゆうびんきょく', 'こうえん', 'としょかん', 'びじゅつかん', 'はくぶつかん',
                  'レストラン', 'ホテル', 'デパート', 'スーパー', 'コンビニ']
places = find_entries(place_readings)
if places:
    semantic_groups['nouns_places'] = {
        'description': 'Common place nouns (house, room, city, station, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in places],
        'entry_ids': [e['id'] for e in places],
        'current_tiers': count_tiers(places),
        'count': len(places),
        'expected': 21
    }

# 29. Common nouns - people
people_readings = ['ひと', 'おとこ', 'おんな', 'おとこのこ', 'おんなのこ', 'こども', 'おとな', 'ともだち', 'せんせい', 'がくせい',
                   'いしゃ', 'けいさつ', 'うんてんしゅ', 'てんいん', 'きゃく', 'しゃちょう', 'ぶちょう', 'かちょう']
people = find_entries(people_readings)
if people:
    semantic_groups['nouns_people'] = {
        'description': 'Common people nouns (person, man, woman, child, friend, etc.)',
        'target_tier': 'basic (common), core (specific roles)',
        'entries': [e['reading'] for e in people],
        'entry_ids': [e['id'] for e in people],
        'current_tiers': count_tiers(people),
        'count': len(people),
        'expected': 18
    }

# 30. Common nouns - things
thing_readings = ['もの', 'こと', 'ところ', 'とき', 'ひ', 'としい', 'みず', 'ごはん', 'たべもの', 'のみもの',
                  'ほん', 'しんぶん', 'ざっし', 'てがみ', 'でんわ', 'けいたい', 'パソコン', 'テレビ', 'くるま', 'でんしゃ']
things = find_entries(thing_readings)
if things:
    semantic_groups['nouns_things'] = {
        'description': 'Common thing nouns (thing, matter, place, time, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in things],
        'entry_ids': [e['id'] for e in things],
        'current_tiers': count_tiers(things),
        'count': len(things),
        'expected': 20
    }

# 31. Conjunctions
conj_readings = ['そして', 'でも', 'しかし', 'だから', 'それで', 'それから', 'または', 'あるいは', 'つまり', 'たとえば']
conjs = find_entries(conj_readings)
if conjs:
    semantic_groups['conjunctions'] = {
        'description': 'Common conjunctions (and, but, so, therefore, etc.)',
        'target_tier': 'basic (common), core (formal)',
        'entries': [e['reading'] for e in conjs],
        'entry_ids': [e['id'] for e in conjs],
        'current_tiers': count_tiers(conjs),
        'count': len(conjs),
        'expected': 10
    }

# 32. Nature words
nature_readings = ['やま', 'かわ', 'うみ', 'そら', 'もり', 'き', 'はな', 'いし', 'つき', 'ほし', 'たいよう', 'ひ', 'あめ', 'ゆき', 'かぜ', 'くも']
nature = find_entries(nature_readings)
if nature:
    semantic_groups['nouns_nature'] = {
        'description': 'Nature words (mountain, river, sea, sky, etc.)',
        'target_tier': 'basic',
        'entries': [e['reading'] for e in nature],
        'entry_ids': [e['id'] for e in nature],
        'current_tiers': count_tiers(nature),
        'count': len(nature),
        'expected': 16
    }

# 33. Animals
animal_readings = ['いぬ', 'ねこ', 'とり', 'さかな', 'うま', 'うし', 'ぶた', 'さる', 'ねずみ', 'うさぎ', 'くま', 'ぞう', 'ライオン', 'とら']
animals = find_entries(animal_readings)
if animals:
    semantic_groups['nouns_animals'] = {
        'description': 'Common animals (dog, cat, bird, fish, etc.)',
        'target_tier': 'basic (common), core (others)',
        'entries': [e['reading'] for e in animals],
        'entry_ids': [e['id'] for e in animals],
        'current_tiers': count_tiers(animals),
        'count': len(animals),
        'expected': 14
    }

# 34. Foods
food_readings = ['にく', 'さかな', 'やさい', 'くだもの', 'たまご', 'パン', 'ごはん', 'ラーメン', 'そば', 'うどん',
                 'すし', 'みそしる', 'さとう', 'しお', 'しょうゆ', 'みそ']
foods = find_entries(food_readings)
if foods:
    semantic_groups['nouns_foods'] = {
        'description': 'Common food words (meat, fish, vegetables, fruit, etc.)',
        'target_tier': 'basic (common), core (specific)',
        'entries': [e['reading'] for e in foods],
        'entry_ids': [e['id'] for e in foods],
        'current_tiers': count_tiers(foods),
        'count': len(foods),
        'expected': 16
    }

# Print summary
print(f"\n{'='*60}")
print(f"SEMANTIC GROUP INVENTORY SUMMARY")
print(f"{'='*60}\n")

total_in_groups = 0
for name, data in sorted(semantic_groups.items()):
    print(f"\n{name}:")
    print(f"  Description: {data['description']}")
    print(f"  Target tier: {data['target_tier']}")
    print(f"  Found: {data['count']} (expected: {data['expected']})")
    print(f"  Current tiers: {data['current_tiers']}")
    print(f"  Entries: {', '.join(data['entries'][:10])}{'...' if len(data['entries']) > 10 else ''}")
    total_in_groups += data['count']

print(f"\n{'='*60}")
print(f"TOTAL ENTRIES IN SEMANTIC GROUPS: {total_in_groups}")
print(f"{'='*60}\n")

# Save to JSON
with open('build/tier_analysis/semantic_groups.json', 'w') as f:
    json.dump(semantic_groups, f, ensure_ascii=False, indent=2)
print(f"Saved semantic groups to build/tier_analysis/semantic_groups.json")
