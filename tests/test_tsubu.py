import pytest

from language.ryuushi import Iwanai, Kana, Kanji
from language.tsubu import Tsubu
from language import kanas
from parsing_tools import recursive_kanas

from tests import kanji_text


@pytest.fixture
def text():
    return kanji_text.text()[0]


def test_kana():
    class K_ka(Kana):
        _kao = "カ"

    ka = K_ka()
    assert ka.kao == ka.onsei
    assert kanas.K_ka.kao == ka.kao
    assert isinstance(kanas.kanas["カ"], Kana)
    assert kanas.kanas["カ"].kao == "カ"


def test_kanji():
    class U31890(Kanji):
        _kao = "粒"
        radical = "米 ˾こめ̚: rice"
        onyomi = ["リュウ"]
        kunyomi = ["つぶ"]
        hint = "One grain 米 standing alone 立"

    tsu = U31890()
    tsu.onsei = "つぶ"
    tsu.imi = "grain"

    assert tsu.kao == "粒"
    assert tsu.onsei == "つぶ"
    assert tsu.imi == "grain"


def test_kao(text):
    # class U31890(Kanji):
    #     _kao = "粒"
    #
    # class U23376(Kanji):
    #     _kao = "子"
    #
    # class Hda(Kana):
    #     _kao = "だ"

    U31890 = type("U31890", (Kanji,), {'_kao': "粒"})
    U23376 = type("U23376", (Kanji,), {'_kao': "子"})
    Comma = type("Comma", (Iwanai,), {'_kao': "、"})
    Hda = type("Hda", (Kana,), {'_kao': "だ"})

    riuu = U31890()
    shi = U23376()
    comma = Comma()
    da = Hda()

    riuushi = Tsubu((riuu, shi), imi="grain")
    pause = Tsubu((riuushi, comma), imi="grain,")
    its_grain = Tsubu((pause, da), imi="it's grain",
                      onsei=["りゅう", "し", "だ"])

    assert its_grain.kao == "粒子、だ"
    assert its_grain.onsei == "りゅうしだ"
    assert its_grain.imi == "it's grain"
    with pytest.raises(ValueError):
        its_grain.onsei = ["りゅう", "し", "x"]

    print(text.kao)


def test_onsei(text):
    print("\n", text.onsei)


def test_imi(text):
    def len2len(tsubu: Tsubu):
        l_factor = 1.625
        if hasattr(tsubu, "_uchiryuu"):
            for shi in tsubu._uchiryuu:
                len2len(shi)
        else:
            print(" -o-")
        print(f"kao: {tsubu.kao}...\nimi: {tsubu.imi}'''")
        print(f" - {len(tsubu) * l_factor} vs imi {len(tsubu.imi)}")
    print()
    len2len(text)


def test_agrupate(text):
    big_tsubu = Tsubu(recursive_kanas(text.kao))
    assert big_tsubu.kao == text.kao
    extract = big_tsubu._uchiryuu[:7]
    new_tsubu = big_tsubu.agrupate(extract, imi="Aincrad")
    assert big_tsubu._uchiryuu[0].imi == "Aincrad"
