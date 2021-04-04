from language.ryuushi import Kanji
from language.tsubu import Tsubu
from mitoushi import escribir, kake


k1 = type("U30011", (Kanji,),
          {'_kao': "画",
           'hint': "Oil painting in a frame",
           'radical': "container",
           'onyomi': ["ガ", "カク"],
           'meanings': ["picture"]})()

k2 = type("U32773", (Kanji,),
          {'_kao': "者",
           'hint': "Most people work daily",
           'radical': "old",
           'onyomi': ["シャ"],
           'kunyomi': ["もの"],
           'meanings': ["person"]})()

painter = Tsubu((k1, k2), imi="painter", onsei=["が", "しゃ"])

kake(escribir([painter]))
