from language.ryuushi import Kana


kanas = {}


def kana_to_globals(kana_str, kana_name):
    globals()[kana_name] = type(
        kana_name, (Kana,), {'_kao': kana_str})()


katakana = {
    "a": "ア", "i": "イ", "u": "ウ", "e": "エ", "o": "オ",
    "ka": "カ", "ki": "キ", "ku": "ク", "ke": "ケ", "ko": "コ",
    "kya": "キャ", "kyu": "キュ", "kyo": "キョ",
    "ga": "ガ", "gi": "ギ", "gu": "グ", "ge": "ゲ", "go": "ゴ",
    "gya": "ギャ", "gyu": "ギュ", "gyo": "ギョ",
    "sa": "サ", "shi": "シ", "su": "ス", "se": "セ", "so": "ソ",
    "sha": "シャ", "shu": "シュ", "sho": "ショ",
    "za": "ザ", "ji": "ジ", "zu": "ズ", "ze": "ゼ", "zo": "ゾ",
    "ja": "ジャ", "ju": "ジュ", "jo": "ジョ",
    "ta": "タ", "chi": "チ", "tsu": "ツ", "tsu_ko": "ッ", "te": "テ", "to": "ト",
    "cha": "チャ", "chu": "チュ", "cho": "チョ",
    "da": "ダ", "di": "ディ", "dzu": "ヅ", "de": "デ", "do": "ド",
    "dya": "ヂャ", "dyu": "ヂュ", "dyo": "ヂョ",
    "na": "ナ", "ni": "ニ", "nu": "ヌ", "ne": "ネ", "no": "ノ",
    "nya": "ニャ", "nyu": "ニュ", "nyo": "ニョ",
    "ha": "ハ", "hi": "ヒ", "fu": "フ", "he": "ヘ", "ho": "ホ",
    "hya": "ヒャ", "hyu": "ヒュ", "hyo": "ヒョ",
    "ba": "バ", "bi": "ビ", "bu": "ブ", "be": "ベ", "bo": "ボ",
    "bya": "バャ", "byu": "バュ", "byo": "バョ",
    "pa": "パ", "pi": "ピ", "pu": "プ", "pe": "ペ", "po": "ポ",
    "pya": "パャ", "pyu": "パュ", "pyo": "パョ",
    "ma": "マ", "mi": "ミ", "mu": "ム", "me": "メ", "mo": "モ",
    "mya": "ミャ", "myu": "ミュ", "myo": "ミョ",
    "ya": "ヤ", "yu": "ユ", "yo": "ヨ",
    "ra": "ラ", "ri": "リ", "ru": "ル", "re": "レ", "ro": "ロ",
    "wa": "ワ", "wo": "ヲ", "n": "ン",
    "v": "ヴ", "va": "ヴァ", "vi": "ヴィ", "vu": "ヴゥ", "ve": "ヴェ", "vo": "ヴォ",
    "dash": "ー"
}

hiragana = {
    "a": "あ", "i": "い", "u": "う", "e": "え", "o": "お",
    "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
    "kya": "きゃ", "kyu": "きゅ", "kyo": "きょ",
    "ga": "が", "gi": "ぎ", "gu": "ぐ", "ge": "げ", "go": "ご",
    "gya": "ぎゃ", "gyu": "ぎゅ", "gyo": "ぎょ",
    "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ",
    "sha": "しゃ", "shu": "しゅ", "sho": "しょ",
    "za": "ざ", "ji": "じ", "zu": "ず", "ze": "ぜ", "zo": "ぞ",
    "ja": "じゃ", "ju": "じゅ", "jo": "じょ",
    "ta": "た", "chi": "ち", "tsu": "つ", "tsu_ko": "っ", "te": "て", "to": "と",
    "cha": "ち", "chu": "ちゅ", "cho": "ちょ",
    "da": "だ", "di": "ぢ", "dzu": "づ", "de": "で", "do": "ど",
    "dya": "ぢゃ", "dyu": "ぢゅ", "dyo": "ぢょ",
    "na": "な", "ni": "に", "nu": "ぬ", "ne": "ね", "no": "の",
    "nya": "にゃ", "nyu": "にゅ", "nyo": "にょ",
    "ha": "は", "hi": "ひ", "fu": "ふ", "he": "へ", "ho": "ほ",
    "hya": "ひゃ", "hyu": "ひゅ", "hyo": "ひょ",
    "ba": "ば", "bi": "び", "bu": "ぶ", "be": "べ", "bo": "ぼ",
    "bya": "びゃ", "byu": "びゅ", "byo": "びょ",
    "pa": "ぱ", "pi": "ぴ", "pu": "ぷ", "pe": "ぺ", "po": "ぽ",
    "pya": "ぴゃ", "pyu": "ぴゅ", "pyo": "ぴょ",
    "ma": "ま", "mi": "み", "mu": "む", "me": "め", "mo": "も",
    "mya": "みゃ", "myu": "みゅ", "myo": "みょ",
    "ya": "や", "yu": "ゆ", "yo": "よ",
    "ra": "ら", "ri": "り", "ru": "る", "re": "れ", "ro": "ろ",
    "rya": "りゃ", "ryu": "りゅ", "ryo": "りょ",
    "wa": "わ", "wo": "を", "n": "ん"
}


for prefix, kana_dict in zip(("K_", "H_"), (katakana, hiragana)):
    for na, on in kana_dict.items():
        kana_to_globals(on, prefix + na)
        kanas[on] = globals()[prefix + na]