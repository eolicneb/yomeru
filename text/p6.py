from language.kanas import kanas, kanas_list
from language.ryuushi import Ryuushi
from language.tsubu import Tsubu
from text.used_kanjis import *

kao = ("初めて《結婚システム》を採用したゲームタイトルが"
       "何なのかは知らないが、もう二十年以上も前から、"
       "ＭＭＯ世界でのキャラクター同士の結婚はとても"
       "ポピュラーなものになっている。")

first = Tsubu([kanjis['初']()], onsei=["はじ"], imi="first")
in_the_beginning = Tsubu([first, *kanas_list("めて")],
                         imi="in the beginning")

marriage = Tsubu([kanjis['結'](), kanjis['婚']()],
                 onsei=["け", "っこん"], imi="marriage")
marriage_system = Tsubu([chevron_o, marriage, *kanas_list("システム"), chevron_c],
                        imi="marriage system")

recruitment = Tsubu([kanjis['採'](), kanjis['用']()],
                    onsei=["さい", "よう"], imi="recruitment")
adopted = Tsubu([recruitment, *kanas_list("した")], imi="adopted")
adopted_system = Tsubu([marriage_system, kanas['を'], adopted])

game_title = Tsubu(kanas_list("ゲームタイトル"), imi="game title")

first_title_adopting = Tsubu([in_the_beginning, adopted_system,
                              game_title, kanas['が']],
                             imi=("the first game title that "
                                  "adopted the marriage system"))

what = Tsubu([kanjis['何']()], onsei=["なに"], imi="what")
of_what = Tsubu([what, *kanas_list("なの")], imi="of what type")

dont_know = Tsubu([kanjis['知'](), *kanas_list("らない")],
                  onsei=["し", None, None, None], imi="don't know")

if_first_title = Tsubu([first_title_adopting, of_what,
                        *kanas_list("かは"), dont_know],
                       imi=("I don't know which was the first game title "
                            "adopting the marriage system"))

already = Tsubu(kanas_list("もう"), imi="already")

twentys = Tsubu([kanjis['二'](), kanjis['十'](), kanjis['年']()],
                onsei=["に", "じゅう", "ねん"], imi="20-year-old")
more_than = Tsubu([kanjis['以'](), kanjis['上']()],
                  onsei=["い", "じょう"], imi="more than")
before = Tsubu([kanjis['前']()], onsei=["まえ"], imi="before")
twenty_and_less = Tsubu([already, twentys, more_than,
                         kanas['も'], before, *kanas_list("から")],
                        imi="those with 20 years and even less")
MMO = Ryuushi()
MMO._kao = "ＭＭＯ"
world = Tsubu([kanjis['世'](), kanjis['界']()],
              onsei=["せい", "かい"], imi="world")
mmo_world = Tsubu([MMO, world], imi="MMO world")
character = Tsubu(kanas_list("キャラクター"), imi="character")
world_character = Tsubu([mmo_world, *kanas_list("での"), character],
                        imi="characters from MMO worlds")

to_each_other = Tsubu([kanjis['同'](), kanjis['士']()],
                     onsei=["どう", "し"], imi="to each other")
marriage = Tsubu([kanjis['結'](), kanjis['婚']()],
                 onsei=["けっ", "こん"], imi="marriage")
marriage_mmo = Tsubu([world_character, to_each_other, kanas['の'], marriage],
                     imi="marriage between characters of MMO worlds")

very = Tsubu(kanas_list("とても"), imi="very")
popular = Tsubu(kanas_list("ポピュラー"), imi="popular")
thing = Tsubu(kanas_list("もの"), imi="thing")
popular_thing = Tsubu([very, popular, kanas['な'], thing],
                      imi="a very popular thing")
is_becoming = Tsubu(kanas_list("なっている"), imi="is becoming")

marriage_becoming = Tsubu([twenty_and_less, comma, marriage_mmo,
                           kanas['は'], popular_thing, kanas['に'], is_becoming],
                          imi="for people in their 20s and even younger, "
                              "marriage between MMO world characters is "
                              "becoming very popular.")

temp = Ryuushi()
temp._kao = ""

honbun = Tsubu([if_first_title, kanas['が'], comma, marriage_becoming, stop])

assert honbun.kao == kao, (f"honbun's kao is different from original"
                           f"\n{honbun.kao}\n{kao}")
