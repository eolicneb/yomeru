from language import kanas
from language.ryuushi import Ryuushi
from language.tsubu import Tsubu
from text.used_kanjis import *

kao = ("俺、レベル96片手剣使い(ソードマン)キリトは、"
       "レベル94細剣使い(フェンサー)アスナに求婚(プロポーズ)し、"
       "承諾された。")

me = Tsubu([kanjis['俺'](), comma], onsei=["おれ"], imi="me")

level96 = Tsubu([*kanas.kanas_list("レベル"),
                 kanjis['9'](),
                 kanjis['6']()],
                onsei=[None, None, None, "きゅうじゅう", "ろく"],
                imi="level 96")

one_hand = Tsubu([kanjis['片'](), kanjis['手']()],
                 onsei=["かた", "て"],
                 imi="one hand")
sword = kanjis['剣']()
sword.onsei = "けん"
sword.imi = "sword"
one_hand_sword = Tsubu([one_hand, sword], imi="one-handed sword")
man = kanjis['使']()
man.onsei = "つか"
man.imi = "user"
sword_wielder = Tsubu([one_hand_sword, man, kanas.kanas['い']()],
                      imi="one-handed sword wielder")
swordman = Tsubu([parenth_o, *kanas.kanas_list("ソードマン"), parenth_c],
                 imi="swordman")
kirito = Tsubu(kanas.kanas_list("キリト"), imi="Kirito")
me_kirito = Tsubu([me, level96, sword_wielder, swordman,
                   kirito, kanas.kanas['は'](), comma],
                  imi="I, the level 96 one-handed sword wielder Kirito,")

level94 = Tsubu([*kanas.kanas_list("レベル"),
                 kanjis['9'](),
                 kanjis['4']()],
                onsei=[None, None, None, "きゅうじゅう", "よん"],
                imi="level 94")
rapier = Tsubu([kanjis['細'](), kanjis['剣']()],
               onsei=["ほそ", "けん"], imi="rapier")
rapier_wielder = Tsubu([rapier, man, kanas.kanas['い']()],
                       imi="rapier wielder")
fencer = Tsubu([parenth_o, *kanas.kanas_list("フェンサー"), parenth_c],
               imi="fencer")
asuna = Tsubu(kanas.kanas_list("アスナ"),
              imi="Asuna")
proposal = Tsubu([kanjis['求'](), kanjis['婚']()],
                 onsei=["きゅう", "こん"], imi="proposal")
propose = Tsubu([parenth_o, *kanas.kanas_list("プロポーズ"), parenth_c],
                imi="propose")
marriage_proposal = Tsubu([proposal, propose, kanas.kanas['し']()],
                          imi="marriage proposal")
to_asuna = Tsubu([level94, rapier_wielder, fencer, asuna,
                  kanas.kanas['に'](), marriage_proposal, comma],
                 imi="proposal to the level 94 fencer Asuna,")

consent = Tsubu([kanjis['承'](), kanjis['諾']()],
                onsei=["しょう", "だく"], imi="consent")
was_given = Tsubu(kanas.kanas_list("された"), imi="was given")
was_accepted = Tsubu([consent, was_given], imi="was accepted")

honbun = Tsubu([me_kirito, to_asuna, was_accepted, stop],
               imi=("I'm the level 96 one-handed sword wielder Kirito, "
                    "and my marriage proposal to the level 94 fencer Asuna "
                    "has been accepted"))
