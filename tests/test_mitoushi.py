import pytest
from math import ceil

from language.tsubu import Tsubu
from mitoushi import KaketaiTsubu, KaiteKanji

from tests import kanji_text as test_text


def len2len(tsubu: Tsubu):
    display = {'kao': "", 'onsei': "", 'imi': []}
    if hasattr(tsubu, "_uchiryuu"):
        for shi in tsubu._uchiryuu:
            len2len(shi)
    else:
        print(" -o-")
    shi = KaketaiTsubu(tsubu)
    print(f"onsei: {kanji_line(str(tsubu.onsei), shi.max_len)}")
    print(f"kao:   {kanji_line(str(tsubu.kao), shi.max_len)}")
    print(f"imi:   {plain_line(str(tsubu.imi), shi.max_len)}")
    print(f"max_len: {shi.max_len}")


def kaite_display(display_dict):
    print(display_dict['onsei'])
    print(display_dict['kao'])
    for imi in display_dict['imi']:
        print(imi)


def kaite(tsubu: Tsubu):
    display = {'kao': KaiteKanji(""),
               'onsei': KaiteKanji(""),
               'imi': []}
    total_len = KaketaiTsubu(tsubu).max_len

    if hasattr(tsubu, "_uchiryuu"):

        extra_len = max(len(tsubu.imi) - total_len, 0) / len(tsubu._uchiryuu)
        running_imi, running_len = [], []
        for shi in tsubu._uchiryuu:
            shi_display = kaite(shi)
            for key in ('kao', 'onsei'):
                shi_display[key].add_space(extra_len)
                display[key] += shi_display[key]
            running_imi.append(shi_display['imi'])
            running_len.append(shi_display['len'])

        level = 0
        while True:
            if not any(len(imi) > level for imi in running_imi):
                break
            display['imi'].append(
                "|".join(plain_line((imi[level]
                                     if len(imi) > level
                                     else ""),
                                    imi_len + extra_len)
                         for imi, imi_len in zip(running_imi, running_len)))
            level += 1

    else:

        display['kao'] = KaiteKanji(tsubu.kao, total_len)
        display['onsei'] = KaiteKanji(
            tsubu.onsei if tsubu.onsei is not None else "",
            total_len)

    if tsubu.imi:
        display['imi'].append(plain_line(tsubu.imi,
                                         max(len(tsubu.imi), total_len)))
    display['len'] = max(total_len, len(tsubu.imi))
    print("-" * round(total_len))
    kaite_display(display)
    return display


def kanji_line(kanji_text, length):
    l_factor = 1.625
    len_kanji_text = ceil(len(kanji_text) * l_factor)
    return extend_line(kanji_text, (length - len_kanji_text))


def plain_line(plain_text, length):
    return extend_line(plain_text, (length - len(plain_text)))


def extend_line(text, extra_length):
    len_space = extra_length / 2.0
    return " " * round(len_space) + text + " " * ceil(len_space)


@pytest.fixture
def text():
    return test_text.text()


@pytest.mark.skip
def test_kanji_retsu(text):
    print()
    len2len(text)


def test_kaite(text):
    print()
    display = kaite(text)
    print(display['onsei'])
    print(display['kao'])
    for imi in display['imi']:
        print(imi)
