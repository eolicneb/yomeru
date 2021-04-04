from .ryuushi import Kanji


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
        assert isinstance(kao, str)
        attrs = {'_kao': kao}
        print(f"Attributes for {kao}:")
        for attr, type_ in self.__attribs.items():
            value = input(f"  {attr}?  ")
            value = value if value else ""
            if type_ == list:
                value = [val.strip() for val in value.split(",")]
            attrs[attr] = value
        return attrs
