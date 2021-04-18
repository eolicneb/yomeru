from language.ryuushi import Ryuushi, Iwanai
from language.kanas import kanas

from text import used_kanjis as uk

from text.p5 import kao

listed = {k: v for k, v in uk.__dict__.items()
          if isinstance(v, (Ryuushi, type))}

iwanai = [r._kao for r in uk.__dict__.values()
          if isinstance(r, Iwanai)]


def list_missings(kao):
    missings = [(k, c) for k in kao
                if (c := f"U{ord(k)}") not in listed
                and k not in kanas
                and k not in iwanai]
    return missings


for k, u in list_missings(kao):
    print(f"{u} = type('{u}', (Kanji,), {{'_kao': '{k}', 'imi': ''}})")
