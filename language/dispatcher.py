from .ryuushi import Iwanai, Kanji, Kana, Ryuushi
from .kanas import kanas
from .kanjis import is_kanji
from text.used_kanjis import iwanai, kanjis


class RyuushiDispatcher:
    """
    Given a str item, it will return the proper type to represent and manipulate that str item.
    """
    def __init__(self, kana_dict, iwanai_dict, kanji_dict):
        self.kana = kana_dict
        self.iwanai = iwanai_dict
        self.kanji = kanji_dict

    def __getitem__(self, item):
        if item in self.kana:
            return self.kana[item]
        if item in self.iwanai:
            return self.iwanai[item]
        if item in self.kanji:
            return self.kanji[item]()
        if is_kanji(item):
            return self.new_kanji(kao=item)
        val = Ryuushi()
        val._kao = item
        return val

    def new_kanji(self, kao: str):
        self.kanji[kao] = type(kao, (Kanji,), {'_kao': kao, 'imi': "", 'onsei': None})
        return self.kanji[kao]


ryuushi_dispatcher = RyuushiDispatcher(kanas, iwanai, kanjis)
