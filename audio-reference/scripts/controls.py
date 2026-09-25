"""Error-injection control clips: readings that deliberately deviate from the
dictionary sentence, used to measure whether STT proof-listening catches real
errors.  All are generated with Gemini 3.8 Flash TTS, female voice.

wrong_reading – the whole sentence is sent as kana with one furigana reading
                swapped for another plausible reading (e.g. こんにち→きょう),
                forcing the TTS to say the wrong reading.
omission / substitution / insertion / repetition – the kanji sentence is edited
                and sent as plain text."""

# (sentence n, correct reading, wrong reading)
WRONG_READINGS = [
    (1, "こんにち", "きょう"), (2, "あす", "あした"), (3, "みょうにち", "あした"),
    (4, "うわて", "じょうず"), (6, "いちば", "しじょう"), (7, "ついたち", "いちにち"),
    (8, "さくじつ", "きのう"), (9, "ゆうべ", "さくや"), (10, "おおごと", "だいじ"),
    (11, "ふるさと", "こきょう"), (12, "もみじ", "こうよう"), (14, "さむけ", "かんき"),
    (15, "しきし", "いろがみ"), (16, "もなか", "さいちゅう"), (18, "ふたえ", "にじゅう"),
    (20, "ふんべつ", "ぶんべつ"), (21, "もっか", "めした"), (22, "せろん", "よろん"),
    (23, "りやく", "りえき"), (24, "かざぐるま", "ふうしゃ"), (27, "にっぽん", "にほん"),
    (30, "からだ", "しんたい"), (32, "じゅっぷん", "じゅうぶん"), (38, "みそか", "さんじゅうにち"),
    (41, "つらい", "からい"), (45, "わたくし", "わたし"), (46, "はたち", "にじゅっさい"),
    (47, "はつか", "にじゅうにち"), (51, "としつき", "ねんげつ"), (58, "ひたい", "がく"),
]

# (sentence n, kind, original substring, replacement)
TEXT_EDITS = [
    (86, "omission", "いつも", ""),
    (88, "omission", "前の車に", ""),
    (99, "omission", "とても", ""),
    (26, "omission", "心より", ""),
    (85, "omission", "ついに", ""),
    (100, "omission", "駅前の", ""),
    (84, "omission", "穴から先が見通せることから", ""),
    (87, "omission", "収納を上手に使うのが大切です。", ""),
    (76, "substitution", "東と西", "北と西"),
    (97, "substitution", "寒い", "暑い"),
    (62, "substitution", "3時", "4時"),
    (42, "substitution", "明るく", "暗く"),
    (33, "substitution", "修理", "掃除"),
    (95, "substitution", "三枚", "二枚"),
    (98, "insertion", "私より", "私よりずっと"),
    (35, "insertion", "茶碗蒸しに", "茶碗蒸しにたくさん"),
    (91, "insertion", "持たせている", "毎月持たせている"),
    (79, "insertion", "ご健勝", "ご健勝とご活躍"),
    (1, "repetition", "会社が", "会社が、会社が"),
    (19, "repetition", "到着した", "到着した、到着した"),
]


def control_jobs(sentences):
    by_n = {s["n"]: s for s in sentences}
    jobs = []

    def job(tag, s, prompt, kind, detail):
        return {"key": f"flash/control/female/{s['n']:03d}_{s['id']}_{tag}",
                "model": "flash", "strategy": "control", "voice": "female",
                "n": s["n"], "id": s["id"], "prompt": prompt,
                "control_kind": kind, "control_detail": detail}

    for n, right, wrong in WRONG_READINGS:
        s = by_n[n]
        assert s["kana"].count(right) == 1, (n, right, s["kana"])
        jobs.append(job("wr", s, s["kana"].replace(right, wrong), "wrong_reading",
                        f"{right} → {wrong}"))
    for n, kind, old, new in TEXT_EDITS:
        s = by_n[n]
        assert s["plain"].count(old) == 1, (n, old)
        detail = f"{old} → {new or '∅'}"
        jobs.append(job(kind[:3], s, s["plain"].replace(old, new), kind, detail))
    return jobs
