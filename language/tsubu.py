from __future__ import annotations
from language.ryuushi import Ryuushi, Iwanai


class Tsubu(Ryuushi):  # 粒: grain
    _kao = ""

    def __init__(self, uchiryuu: list, onsei=None, imi=""):
        self._len = None
        self._hyoushi = None  # 拍子: rhythm (musical tempo)
        self._uchiryuu = uchiryuu  # 内粒: inner grains
        super().__init__()
        self.imi = imi
        if onsei:
            self.onsei = onsei

    @property
    def onsei(self):
        return "".join(ryuushi.onsei for ryuushi in self._uchiryuu
                       if not isinstance(ryuushi, Iwanai))

    @onsei.setter
    def onsei(self, onsei):
        if onsei is None:
            onsei = [None] * self.hyoushi
        else:
            assert self.hyoushi == len(onsei), (
                f"'onsei' length ({len(onsei)}) different"
                f" from self lenght ({self.hyoushi})")
        point = 0
        for ryuushi in self._uchiryuu:
            if isinstance(ryuushi, Iwanai):
                continue
            if not isinstance(ryuushi, Tsubu):
                ryuushi.onsei = onsei[point]
                point += 1
            else:
                start, point = point, ryuushi.hyoushi + point
                ryuushi.onsei = onsei[start:point]

    @property
    def kao(self):
        return "".join(ryuushi.kao for ryuushi in self._uchiryuu)

    def __len__(self):
        if not self._len:
            self._len = sum(len(ryuushi)
                            for ryuushi in self._uchiryuu)
        return self._len

    def __iter__(self):
        return iter(self._uchiryuu)

    @property
    def hyoushi(self):  # 拍子: rhythm (musical tempo)
        if not self._hyoushi:
            self._hyoushi = sum(ryuushi.hyoushi
                                for ryuushi in self._uchiryuu)
        return self._hyoushi

    @hyoushi.setter
    def hyoushi(self, _):
        return

    def agrupate(self, tsubugun: list, onsei=None, imi=None):  # 粒群: group of grains
        assert all(ko in self._uchiryuu for ko in tsubugun)
        anchor = self._uchiryuu.index(tsubugun[0])
        for ko in tsubugun:
            self._uchiryuu.remove(ko)
        new_tsubu = Tsubu(tsubugun, onsei=onsei, imi=imi)
        self._uchiryuu.insert(anchor, new_tsubu)
        return new_tsubu

    def explode(self, uchiryuu: Tsubu):
        assert uchiryuu in self._uchiryuu
        anchor = self._uchiryuu.index(uchiryuu)
        self._uchiryuu.pop(anchor)
        for tsubu in uchiryuu._uchiryuu[::-1]:
            self._uchiryuu.insert(anchor, tsubu)
