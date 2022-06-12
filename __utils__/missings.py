from language.ryuushi import Ryuushi, Iwanai
from language.kanas import kanas


class Missing:
    def __init__(self, used_kanji):
        self.listed = {k: v for k, v in used_kanji.items()
                       if isinstance(v, (Ryuushi, type))}

        self.iwanai = [r._kao for r in used_kanji.values()
                       if isinstance(r, Iwanai)]

    def list_missing(self, kao):
        missing = [(k, c) for k in kao
                   if (c := self.kanji_class_name(k)
                       not in self.listed)
                   and k not in kanas
                   and k not in self.iwanai]
        return missing

    @staticmethod
    def kanji_class_name(k):
        return f"U{ord(k)}"

    @classmethod
    def kanji_class_string(cls, k):
        name = cls.kanji_class_name(k)
        return (f"{name} = type('{name}', (Kanji,),"
                f" {{'_kao': '{k}', 'imi': ''}})")


if __name__ == "__main__":
    import os
    import pathlib
    from text import used_kanjis as uk
    from add_page import AddPage

    root = pathlib.Path(os.getcwd()).parent
    text_dir = root / "text"
    filename = f"p{AddPage.get_last_page(str(text_dir))}.py"

    exec(open(text_dir / filename, encoding="utf8").read())

    used_kanji = uk.__dict__
    missing_kanji = Missing(used_kanji)

    for k, _ in missing_kanji.list_missing(kao):
        print(missing_kanji.kanji_class_string(k))
