import json

import pytest

import bs4

from language.tsubu import Tsubu
from language.dispatcher import ryuushi_dispatcher as ryuushi_dict
from language.hanasu import Honbun

from mitoushi import insert_bun
import tests.kanji_text as test_text


@pytest.fixture
def text():
    return test_text.text()


@pytest.fixture
def json_data():
    return json.load(open("test.json", "r"))


# @pytest.mark.skip
def test_table(text, caplog):
    to_html(text, "test.html")


def to_html(text, outfile_name):
    doc = bs4.BeautifulSoup('''
    <!DOCTYPE html>
        <header>
            <meta charset="UTF-8">
            <style/>
        </header>
        <body>
            <div>''')
    doc.header.style.string = open("test.css", "r").read()
    [insert_bun(bun, doc.div, doc) for bun in text]
    with open(outfile_name, "w", encoding="utf8") as f:
        f.write(doc.prettify())


def test_to_json(text):
    from pprint import pprint
    json_tsubu = [to_json(bun) for bun in text]
    pprint(json_tsubu)
    json.dump(json_tsubu, open('test.json', "w"), indent=2)


def to_json(tsubu):
    if hasattr(tsubu, '_uchiryuu'):
        return {'imi': tsubu.imi,
                'uchiryuu': [to_json(shi) for shi in tsubu._uchiryuu]}
    else:
        return {'imi': tsubu.imi, 'kao': tsubu.kao, 'onsei': tsubu.onsei}


class_dipatcher = {
    ('imi', 'uchiryuu'): "tsubu",
    ('imi', 'kao', 'onsei'): "ryuushi"
}


def make_ryuushi(imi, kao, onsei):
    shi = ryuushi_dict[kao]
    if onsei or imi:
        shi.onsei = onsei
        shi.imi = imi
    return shi


def make_tsubu(imi, uchiryuu):
    def select(object):
        if class_dipatcher[tuple(object.keys())] == "ryuushi":
            return make_ryuushi(**object)
        else:
            return make_tsubu(**object)
    ryuu = [select(obj) for obj in uchiryuu]
    return Tsubu(imi=imi, uchiryuu=ryuu)


def test_from_json(json_data):
    honbun = Honbun()
    honbun.from_dict(json_data)
    to_html(honbun.honbun_list, "from_json.html")
