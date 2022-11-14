from language import kanas
from language.ryuushi import Ryuushi
from language.tsubu import Tsubu
from text.used_kanjis import *

kao = "もちろんこれは、ソードアート・オンラインというＶＲＭＭＯ－ＲＰＧの中での話だ。"

of_course = Tsubu(kanas.kanas_list("もちろん"),
                  imi="of course")
this = Tsubu(kanas.kanas_list("これ"), imi="this")

sao = Tsubu([*kanas.kanas_list("ソードアート"), midpoint,
             *kanas.kanas_list("オンライン")],
            imi="SWORD ART・ONLINE")
say = Tsubu(kanas.kanas_list("いう"), imi="say")
rpg = Ryuushi()
rpg._kao = "ＶＲＭＭＯ－ＲＰＧ"
called_sao = Tsubu([sao, kanas.kanas['と'](), say, rpg],
                   imi="the ＶＲＭＭＯ－ＲＰＧ called SWORD ART・ONLINE")

inside = Tsubu([kanjis['中']()], onsei=["なか"], imi="in")
story = Tsubu([kanjis['話']()], onsei=["はなし"], imi="story")

rpg_called_sao = Tsubu([called_sao, kanas.kanas['の'](), inside, kanas.kanas['で']()],
                       imi="within the ＶＲＭＭＯ－ＲＰＧ called SWORD ART・ONLINE")


temp = Ryuushi()
temp._kao = ""

honbun = Tsubu([of_course, this, kanas.kanas['は'](), comma,
                rpg_called_sao, kanas.kanas['の'](),
                story, kanas.kanas['だ'](), stop],
               imi="Of course, this is a story from within the "
                   "VRMMO-RPG called SWORD ART・ONLINE.")
