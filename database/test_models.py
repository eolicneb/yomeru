from flask_testing import TestCase

from api.main import create_test_app
from database.models import (db, Char, Katakana, Hiragana, Kanji,
                             Ryuushi, Tsubu)


class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return create_test_app()

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

    def test_char(self):
        k = Kanji(kao="J")
        db.session.add(k)
        assert k in list(Char.query.all())

    def test_tsubu(self):
        j = Kanji(kao="J")
        k = Katakana(kao="k")
        r1 = Ryuushi(id="r1", char=j)
        r2 = Ryuushi(id="r2", char=k)
        t1 = Tsubu(id="t1")
        t2 = Tsubu(id="t2", tosa=t1)
        t2.uchiryuu.append(r1)
        t2.uchiryuu.append(r2)
        assert t2 in t1.uchiryuu
        assert r1 in t2.uchiryuu

        def read_tsubu(tsubu):
            for ts in tsubu.uchiryuu:
                for ts_s in read_tsubu(ts):
                    yield ts_s
            if isinstance(tsubu, Ryuushi):
                yield tsubu.char.kao

        assert "".join(read_tsubu(t1)) == "Jk"
