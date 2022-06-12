from parsing_tools import recursive_kanas
from language.kanas import kanas, kanas_list
from language.ryuushi import Ryuushi
from language.tsubu import Tsubu
from text.used_kanjis import *

kao = ("たいていのタイトルでは《夫婦》のキャラクターには何らかの特典が与えられるので、"
       "それ目当てで結婚するケースも多いだろうし、"
       "もちろん真面目なロールプレイの一環として結婚するプレイヤーもいれば、"
       "中にはゲーム内での結婚がきっかけで現実世界でも結婚する例さえあるらしい。")


weird_list = recursive_kanas(kao)
weird_tsubu = Tsubu(weird_list)

# almost_list =


honbun = Tsubu([weird_tsubu])

assert honbun.kao == kao, (f"honbun's kao is different from original"
                           f"\n{honbun.kao}\n{kao}")
