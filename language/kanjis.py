from re import compile
from .ryuushi import Kanji


kanji_regex = compile(r'[\x3400-\x4DB5\x4E00-\x9FCB\xF900-\xFA6A]')


class KanjisDict(dict):
    __attribs = {'radical': str,
                 'hint': str,
                 'onyomi': list,
                 'kunyomi': list,
                 'meanings': list}

    def __getitem__(self, kao):
        assert isinstance(kao, str)
        kao_key = ord(kao)
        if kao_key in self:
            return super().__getitem__(kao_key)

    def make_kanji(self, kao):
        kao_key = ord(kao)

    def ask_attributes(self, kao):
        assert isinstance(kao, str) and is_kanji(kao)
        attrs = {'_kao': kao}
        print(f"Attributes for {kao}:")
        for attr, type_ in self.__attribs.items():
            value = input(f"  {attr}?  ")
            value = value if value else ""
            if type_ == list:
                value = [val.strip() for val in value.split(",")]
            attrs[attr] = value
        return attrs


def is_kanji(char):
    return bool(kanji_regex.match(char))
