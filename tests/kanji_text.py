from language import kanas
from language.ryuushi import Kanji, Iwanai
from language.tsubu import Tsubu


def text():
    kao = "アインクラッド標準時、二〇二四年十月二十三日午後九時。"
    U27161 = type("U27161", (Kanji,), {'_kao': "標", 'imi': "mark"})
    U28310 = type("U28310", (Kanji,), {'_kao': "準", 'imi': "standard"})
    U26178 = type("U26178", (Kanji,), {'_kao': "時", 'imi': "time"})
    U20108 = type("U20108", (Kanji,), {'_kao': "二", 'imi': "two"})
    U12295 = type("U12295", (Kanji,), {'_kao': "〇", 'imi': "zero"})
    U22235 = type("U22235", (Kanji,), {'_kao': "四", 'imi': "four"})
    U24180 = type("U24180", (Kanji,), {'_kao': "年", 'imi': "year"})
    U21313 = type("U21313", (Kanji,), {'_kao': "十", 'imi': "ten"})
    U26376 = type("U26376", (Kanji,), {'_kao': "月", 'imi': "month"})
    U19977 = type("U19977", (Kanji,), {'_kao': "三", 'imi': "three"})
    U26085 = type("U26085", (Kanji,), {'_kao': "日", 'imi': "day"})
    U21320 = type("U21320", (Kanji,), {'_kao': "午", 'imi': "noon"})
    U24460 = type("U24460", (Kanji,), {'_kao': "後", 'imi': "after"})
    U20061 = type("U20061", (Kanji,), {'_kao': "九", 'imi': "nine"})

    comma = type("Comma", (Iwanai,), {'_kao': "、"})()
    stop = type("Stop", (Iwanai,), {'_kao': "。"})()

    aincrad = Tsubu([kanas.kanas['ア'], kanas.kanas['イ'],
                     kanas.kanas['ン'], kanas.kanas['ク'],
                     kanas.kanas['ラ'], kanas.kanas['ッ'],
                     kanas.kanas['ド']],
                    imi="Aincrad")
    std_time = Tsubu([U27161(), U28310(), U26178()],
                     onsei=["ひょう", "じゅん", "じ"],  # Hyōjunji
                     imi="standard time")
    reference = Tsubu([aincrad, std_time])

    year_num = Tsubu([U20108(), U12295(), U20108(), U22235()], imi="2024")
    year = Tsubu([year_num, U24180()],
                 onsei=["に", "れい", "に", "し", "ねん"],
                 imi="year 2024")
    month = Tsubu([U21313(), U26376()],
                  onsei=["じゅう", "がつ"], imi="October")
    day_num = Tsubu([U20108(), U21313(), U19977()],
                    imi="23")
    day = Tsubu([day_num, U26085()],
                onsei=["に", "じゅう", "さん", "にじ"],
                imi="day 23rd")
    date = Tsubu([year, month, day],
                 imi="October 23rd, 2024")

    afternoon = Tsubu([U21320(), U24460()])
    hour = Tsubu([afternoon, U20061(), U26178()],
                 onsei=["ご", "ご", "きゅう", "じ"],  # Gogokyūji
                 imi="9 PM")

    date_time = Tsubu([date, hour], imi="October 23rd, 2024, 9 PM")

    return Tsubu([reference, comma, date_time, stop])