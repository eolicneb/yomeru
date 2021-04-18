import json

import pytest

import bs4

from mitoushi import insert_bun
import tests.kanji_text as test_text


@pytest.fixture
def text():
    return test_text.text()


# @pytest.mark.skip
def test_table(text, caplog):
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
    with open("test.html", "w", encoding="utf8") as f:
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