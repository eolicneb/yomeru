import bs4
from flask import Flask, render_template, request
from language.ryuushi import Ryuushi, Kanji
from mitoushi import insert_bun
import tests.kanji_text as test_text

app = Flask(__name__)


def make_doc(text):
    doc = bs4.BeautifulSoup('<div id="root">', features="html.parser")
    [insert_bun(bun, doc.div, doc) for bun in text]
    return doc.find(id="root").children


@app.route("/web/<path:file_path>")
def serve_file(file_path):
    print(file_path)
    template = render_template(file_path)
    return template


@app.route("/translator")
def translator():
    buns = list(make_doc(test_text.text()))
    template = render_template("botonera.html", buns=buns)
    return template


@app.route("/merge", methods=['POST'])
def merge():
    data = request.get_json()
    print(data)
    parent = Ryuushi.get[data['parent_id']]
    if isinstance(parent, Kanji):
        parent.onsei = data['onsei']
    else:
        print(len(parent._uchiryuu))
        sub_range = [Ryuushi.get[tsubu_id] for tsubu_id in data['range']]
        if sub_range:
            parent.agrupate(sub_range, imi=data['imi'], onsei=data['onsei'])
            print(len(parent._uchiryuu))
        elif isinstance(parent, Kanji):
            parent.onsei = data['onsei']
        else:
            if data['imi'] is not None:
                parent.imi = data['imi']
    doc = bs4.BeautifulSoup('<div id="merge_result">', features="html.parser")
    insert_bun(parent, doc.div, doc)
    return doc.prettify(), 200


@app.route("/unwrap", methods=['POST'])
def unwrap():
    data = request.get_json()
    print(data)
    parent = Ryuushi.get[data['parent_id']]
    print(len(parent._uchiryuu))
    wrapped = Ryuushi.get[data['wrapped_id']]
    parent.explode(wrapped)
    doc = bs4.BeautifulSoup('<div id="merge_result">', features="html.parser")
    insert_bun(parent, doc.div, doc)
    return doc.prettify(), 200
