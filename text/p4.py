from language.kanas import kanas, kanas_list
from language.ryuushi import Ryuushi
from language.tsubu import Tsubu
from text.used_kanjis import *

kao = ("現実世界では俺とアスナは顔を合わせたことさえなく、"
       "そもそも俺は法的に結婚できる年齢に達していない。")

reality = Tsubu([kanjis['現'](), kanjis['実']()],
                onsei=["げん", "じつ"],
                imi="reality")
world = Tsubu([kanjis['世'](), kanjis['界']()],
              onsei=["せ", "かい"],
              imi="world")
real_world = Tsubu([reality, world], imi="real world")
within_real_world = Tsubu([real_world, *kanas_list("では")],
                          imi="within the real world")
me = Tsubu([kanjis['俺']()], onsei=["おれ"], imi="me")
asuna = Tsubu(kanas_list("アスナ"), imi="Asuna")
asuna_and_i = Tsubu([me, kanas['と'](), asuna, kanas['は']()],
                    imi="Asuna and I")

face = Tsubu([kanjis['顔']()], onsei=["かお"], imi="face")
fit = Tsubu([kanjis['合']()], onsei=["あい"], imi="harmony")
could_conbine = Tsubu([fit, *kanas_list("わせた")],
                    imi="could combine")
this = Tsubu(kanas_list("こと"), imi="this")
not_even = Tsubu(kanas_list("さえなく"), imi="not even")
not_face_to_face = Tsubu([face, kanas['を'](), could_conbine,
                          this, not_even],
                         imi="couldn't even see face to face")

first = Tsubu(kanas_list("そもそも"), imi="in first place")

me2 = Tsubu([kanjis['俺'](), kanas['は']()],
            onsei=["おれ", None], imi="I")
in_legal = Tsubu([kanjis['法'](), kanjis['的'](), kanas['に']()],
                 onsei=["ほう", "てき", None], imi="in legal")
marriage = Tsubu([kanjis['結'](), kanjis['婚']()],
                 onsei=["けっ", "こん"], imi="marriage")
possible = Tsubu(kanas_list("できる"), imi="possible")
in_age = Tsubu([kanjis['年'](), kanjis['齢'](), kanas['に']()],
               onsei=["ねん", "れい", None], imi="in age")
legal_age = Tsubu([in_legal, marriage, possible, in_age],
                  imi="in legal age to get married")

attain = Tsubu([kanjis['達'](), *kanas_list("して")],
               onsei=["たっ", None, None], imi="attain-te")
not_attaining = Tsubu([attain, *kanas_list("いない")],
                      imi="not attaining")
not_enough = Tsubu([me2, legal_age, not_attaining, stop],
                   imi="I'm not old enough to get married")

temp = Ryuushi()
temp._kao = ""

honbun = Tsubu([within_real_world, asuna_and_i, not_face_to_face,
                comma, first, not_enough])
