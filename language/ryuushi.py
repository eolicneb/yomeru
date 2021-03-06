class Ryuushi:  # 粒子: particle
    _kao = "-"

    def __init__(self):
        self.onsei = None  # 音声: sound, voice
        self.imi = ""  # 意味: meaning
        self.hyoushi = 1

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
    """
    This class is intended to be passed as a type, so that different positions where a Kanji is used
    can receive a different .onsei and a different .imi.
    """
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
