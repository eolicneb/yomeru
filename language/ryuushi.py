from uuid import uuid1


class Ryuushi:  # 粒子: particle
    get = {}
    _kao = "-"

    def __init__(self):
        self.id = uuid1().hex
        self.onsei = None  # 音声: sound, voice
        self.imi = ""  # 意味: meaning
        self.hyoushi = 1
        Ryuushi.get[self.id] = self

    @property
    def kao(self):
        return self._kao

    def __len__(self):
        return 1


class Iwanai(Ryuushi):  # 言わない: not say
    def __init__(self):
        super().__init__()
        self.hyoushi = 0


class Kana(Ryuushi):  # 仮名: (lit: provisional name)
    _kao = "-"
    _onsei = None

    def __init__(self):
        super().__init__()
        self._onsei = self._kao

    @property
    def onsei(self):
        return self._onsei

    @onsei.setter
    def onsei(self, on):
        if on is None:
            return
        if on != self._onsei:
            raise ValueError(
                f"Wrong onsei '{on}' for {self._kao}.")


class Kanji(Ryuushi):
    _kao = "〇"
    radical = "〇"
    hint = "no hint"
    onyomi = []
    kunyomi = []
    meanings = []

    def __init__(self):
        super().__init__()
        self.imi = self.imi if self.imi else ""
        self.onsei = self.onsei if self.onsei else ""

    @property
    def kao(self):
        return self._kao
