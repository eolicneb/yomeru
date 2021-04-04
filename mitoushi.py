from copy import deepcopy
from math import ceil

from language.tsubu import Tsubu

""" 見通し: outlook, view

The length of lines for regular romaji characters 
and those for kanjis and kanas are in ratio 39:24.
IOW, each kana and kanki "measures" like 1.625
romaji characters.
"""


KANJI_LENGTH_FACTOR = 1.625


class EOL(Exception):
    pass


class KaiteKanji:
    L_FACTOR = KANJI_LENGTH_FACTOR

    def __init__(self, kao, total_len=None):
        self.kao = str(kao)
        self._kao_len = (len(kao)
                         if isinstance(kao, self.__class__)
                         else len(kao) * self.L_FACTOR)
        self._total_len = total_len
        self._margin_space = None

    @property
    def total_len(self):
        if self._total_len is None:
            self._total_len = self.kao_len
        return self._total_len

    @total_len.setter
    def total_len(self, total_len):
        assert total_len >= self.kao_len, \
            (f"The total length {total_len} must not be"
             f" smaller than the text length {self.kao_len}")
        self._total_len = total_len
        self.make_margins()

    def make_margins(self):
        extra_space = (self.total_len - self.kao_len) / 2
        self._margin_space = (round(extra_space),
                              ceil(extra_space))

    def add_space(self, extra_space):
        self.total_len += extra_space

    @property
    def kao_len(self):
        if self._kao_len is None:
            self._kao_len = len(self.kao) * self.L_FACTOR
        return self._kao_len

    def __len__(self):
        return ceil(self.total_len)

    def __str__(self):
        if self._margin_space is None:
            self.make_margins()
        return (" " * self._margin_space[0]
                + str(self.kao)
                + " " * self._margin_space[1])

    def __add__(self, other):
        new_len, new_str = self.add_core(other)
        new = self.__class__(new_str, new_len)
        new._kao_len = new_len
        return new

    def __iadd__(self, other):
        new_len, new_str = self.add_core(other)
        self.kao = new_str
        self._kao_len = self._total_len = new_len
        self._margin_space = (0, 0)
        return self

    def add_core(self, other):
        if not isinstance(other, self.__class__):
            new_len = self.total_len + len(other) * self.L_FACTOR
        else:
            new_len = self.total_len + other.total_len
        new_str = str(self) + str(other)
        return new_len, new_str


class KaketaiTsubu:
    L_FACTOR = KANJI_LENGTH_FACTOR

    def __init__(self, tsubu: [Tsubu]):
        self.tsubu = tsubu
        self.tsubu._max_len = None

    @property
    def max_len(self):
        if self.tsubu._max_len is None:
            self.tsubu._max_len = max(
                self._uchi_len, len(self.tsubu.imi))
        if len(self.tsubu.imi) > len(self.tsubu.kao)*self.L_FACTOR:
            print(self.tsubu.kao, self.tsubu.imi)
        return self.tsubu._max_len

    @property
    def _uchi_len(self):
        if not hasattr(self.tsubu, "_uchiryuu"):
            return self._ryuushi_len(self.tsubu)

        running_len = 0
        for shi in self.tsubu._uchiryuu:
            if hasattr(shi, "_uchiryuu"):
                running_len += self.__class__(shi).max_len
            else:
                running_len += self._ryuushi_len(shi)
        return running_len

    @classmethod
    def _ryuushi_len(cls, shi):
        len_onsei = (len(shi.onsei) * cls.L_FACTOR
                     if shi.onsei else 0)
        len_kao = len(shi.kao) * cls.L_FACTOR
        return ceil(max(len_onsei, len_kao, len(shi.imi)))


class KanjiRetsu:
    L_FACTOR = KANJI_LENGTH_FACTOR

    def __init__(self, max_len=None, len_margin=0.7):
        self._kao = ""
        self.len = 0
        self.max_len = max_len
        self.MARGIN = len_margin

    @property
    def kao(self):
        return self._kao

    def extend(self, other):
        assert isinstance(other, self.__class__), \
            f"{self.__class__} expected, got {other.__class__}"
        if (self.max_len != other.max_len
                or self.MARGIN != other.MARGIN):
            raise ValueError("Only objects with same 'max_len' and "
                             "'len_margin' attributes can be extended.")
        self._kao += other._kao
        self.len += other.len

    def append(self, kanji_text):
        assert isinstance(kanji_text, str), f"Only str can be appended, not {type(kanji_text)}"
        if not kanji_text:
            return
        text_len = self.L_FACTOR * len(kanji_text)
        self.check_new_len(text_len)
        self.len += text_len
        self.check_remainder()

    def check_remainder(self):
        if 1 + int(self.len) - self.len > 1:
            self._kao += " "
            self.len += 1

    def check_new_len(self, text_len):
        if not self.max_len:
            return
        if self.len + text_len > self.max_len + self.MARGIN:
            raise EOL

    def __add__(self, other):
        temp_third = deepcopy(self)
        return temp_third.extend(other)

    def __iadd__(self, other):
        self.extend(other)


class Retsu:  # 列: column
    def __init__(self, max_length=None):
        self.onsei = ""
        self.kao = ""
        self.imi = []
        self.max_length = None
        self.running_length = 0
        self.onsei_len_flag = True
        self.kao_len_flag = True

    def onsei_len(self, kan_text, flag):
        self.k_len_flag = not self.k_len_flag


def kake(retsu: Retsu):
    print(retsu.onsei)
    print(retsu.kao)
    print(retsu.imi)


def escribir(kanas):
    retsu = Retsu()
    for k in kanas:
        retsu.add(k)
    return retsu


to_dict = {'kao': "", 'onsei': "", 'imi': []}


def len2len(tsubu: Tsubu, running_dict):
    structure = {'tsubu': tsubu, 'len': 0}
    if hasattr(tsubu, "_uchiryuu"):
        level, running_retsu = 0, running_dict['kao'][-1]
        for shi in tsubu._uchiryuu:
            sub_level, sub_kao = len2len(shi)
            level = max(level, sub_level)
            try:
                running_retsu += sub_kao
            except EOL:
                running_retsu = KanjiRetsu(max_len=running_retsu.max_len,
                                           len_margin=running_retsu.MARGIN)
                running_dict['kao'].append(running_retsu)
                running_retsu += sub_kao
        level += 1
    else:
        level = 0
    print(f"kao: {tsubu.kao}...\nimi: {tsubu.imi}'''")
    print(f" - {len(tsubu)} vs imi {len(tsubu.imi)}")
    return level, running_retsu
