from language import kanas
from language.tsubu import Tsubu
from text.used_kanjis import *


kao = "アインクラッド標準時、二〇二四年十月二十三日午後九時。"

aincrad = Tsubu(kanas.kanas_list("アインクラッド"),
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

honbun = Tsubu([reference, comma, date_time, stop])
