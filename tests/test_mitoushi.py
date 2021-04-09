import pytest

import bs4

from mitoushi import insert_tsubu
import tests.kanji_text as test_text


@pytest.fixture
def text():
    return test_text.text()


def test_table(text):
    doc = bs4.BeautifulSoup('<!DOCTYPE html><header><meta charset="UTF-8"><style/></header><body><table><tr><td>')
    doc.header.style.string = open("test.css", "r").read()
    insert_tsubu(text, doc.tr.td, doc)
    with open("test.html", "w", encoding="utf8") as f:
        f.write(doc.prettify())
