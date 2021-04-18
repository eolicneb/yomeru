from language.kanas import kanas, kanas_list
from language.ryuushi import Ryuushi
from language.tsubu import Tsubu
from text.used_kanjis import *

kao = "アスナのほうは微妙なところかもしれないが。"

asuna = Tsubu(kanas_list("アスナ"), imi="Asuna")
side = Tsubu(kanas_list("ほう"), imi="side")
asuna_case = Tsubu([asuna, kanas['の'], side, kanas['は']],
                   imi="Asuna's side")

subtle = Tsubu([kanjis['微'](), kanjis['妙'](), kanas['な']],
               onsei=["び", "みょう", None],
               imi="subtle")
place = Tsubu(kanas_list("ところ"), imi="place")

can_know = Tsubu(kanas_list("しれ"), imi="can-know")
cant_know = Tsubu([can_know, *kanas_list("ない")])
perhaps = Tsubu([*kanas_list("かも"), cant_know, kanas['が']],
                imi="perhaps")

temp = Ryuushi()
temp._kao = ""

honbun = Tsubu([asuna_case, subtle, place, perhaps, stop],
               imi="Perhaps Asuna's case is more subtle.")
