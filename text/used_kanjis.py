from language.ryuushi import Kanji, Iwanai

# p1
U27161 = type("U27161", (Kanji,), {'_kao': "標", 'imi': "mark"})
U28310 = type("U28310", (Kanji,), {'_kao': "準", 'imi': "standard"})
U26178 = type("U26178", (Kanji,), {'_kao': "時", 'imi': "time"})
U20108 = type("U20108", (Kanji,), {'_kao': "二", 'imi': "two"})
U12295 = type("U12295", (Kanji,), {'_kao': "〇", 'imi': "zero"})
U22235 = type("U22235", (Kanji,), {'_kao': "四", 'imi': "four"})
U24180 = type("U24180", (Kanji,), {'_kao': "年", 'imi': "year"})
U21313 = type("U21313", (Kanji,), {'_kao': "十", 'imi': "ten"})
U26376 = type("U26376", (Kanji,), {'_kao': "月", 'imi': "moon"})
U19977 = type("U19977", (Kanji,), {'_kao': "三", 'imi': "three"})
U26085 = type("U26085", (Kanji,), {'_kao': "日", 'imi': "sun"})
U21320 = type("U21320", (Kanji,), {'_kao': "午", 'imi': "noon"})
U24460 = type("U24460", (Kanji,), {'_kao': "後", 'imi': "rear"})
U20061 = type("U20061", (Kanji,), {'_kao': "九", 'imi': "nine"})

#p2
U20474 = type('U20474', (Kanji,), {'_kao': '俺', 'imi': 'me'})
U29255 = type('U29255', (Kanji,), {'_kao': '片', 'imi': 'part'})
U25163 = type('U25163', (Kanji,), {'_kao': '手', 'imi': 'hand'})
U21091 = type('U21091', (Kanji,), {'_kao': '剣', 'imi': 'sword'})
U20351 = type('U20351', (Kanji,), {'_kao': '使', 'imi': 'use, envoy'})
U32048 = type('U32048', (Kanji,), {'_kao': '細', 'imi': 'fine'})
U27714 = type('U27714', (Kanji,), {'_kao': '求', 'imi': 'demand'})
U23130 = type('U23130', (Kanji,), {'_kao': '婚', 'imi': 'marry'})
U25215 = type('U25215', (Kanji,), {'_kao': '承', 'imi': 'agree to'})
U35582 = type('U35582', (Kanji,), {'_kao': '諾', 'imi': 'consent'})
U57 = type('U57', (Kanji,), {'_kao': '9', 'imi': ''})
U54 = type('U54', (Kanji,), {'_kao': '6', 'imi': ''})
U57 = type('U57', (Kanji,), {'_kao': '9', 'imi': ''})
U52 = type('U52', (Kanji,), {'_kao': '4', 'imi': ''})

# p3
U20013 = type('U20013', (Kanji,), {'_kao': '中', 'imi': 'in'})
U35441 = type('U35441', (Kanji,), {'_kao': '話', 'imi': 'story'})

# p4
U29694 = type('U29694', (Kanji,), {'_kao': '現', 'imi': 'present'})
U23455 = type('U23455', (Kanji,), {'_kao': '実', 'imi': 'real'})
U19990 = type('U19990', (Kanji,), {'_kao': '世', 'imi': 'world'})
U30028 = type('U30028', (Kanji,), {'_kao': '界', 'imi': 'boundary'})
U38996 = type('U38996', (Kanji,), {'_kao': '顔', 'imi': 'face'})
U21512 = type('U21512', (Kanji,), {'_kao': '合', 'imi': 'fit'})
U27861 = type('U27861', (Kanji,), {'_kao': '法', 'imi': 'law'})
U30340 = type('U30340', (Kanji,), {'_kao': '的', 'imi': 'target'})
U32080 = type('U32080', (Kanji,), {'_kao': '結', 'imi': 'conclude'})
U40802 = type('U40802', (Kanji,), {'_kao': '齢', 'imi': 'age'})
U36948 = type('U36948', (Kanji,), {'_kao': '達', 'imi': 'attain'})

#p5
U24494 = type('U24494', (Kanji,), {'_kao': '微', 'imi': 'fine'})
U22937 = type('U22937', (Kanji,), {'_kao': '妙', 'imi': 'mysterious'})

# iwanai
comma = type("Comma", (Iwanai,), {'_kao': "、"})()
stop = type("Stop", (Iwanai,), {'_kao': "。"})()
midpoint = type("Midpoint", (Iwanai,), {'_kao': "・"})()
parenth_o = type("parenth_open", (Iwanai,), {'_kao': "("})()
parenth_c = type("parenth_close", (Iwanai,), {'_kao': ")"})()

kanjis = {}

locals_copy = list(locals().values())

for kanji_class in locals_copy:
    if isinstance(kanji_class, type) and issubclass(kanji_class, Kanji):
        kanjis[kanji_class._kao] = kanji_class
