from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Char(db.Model):
    __tablename__ = 'char'
    __mapper_args__ = {"polymorphic_identity": "char",
                       "polymorphic_on": "char_type"}

    kao = db.Column(db.String, primary_key=True)
    char_type = db.Column(db.String)


class Katakana(Char):
    __mapper_args__ = {"polymorphic_identity": "katakana"}


class Hiragana(Char):
    __mapper_args__ = {"polymorphic_identity": "hiragana"}


class Iwanai(Char):
    __mapper_args__ = {"polymorphic_identity": "iwanai"}


class Kanji(Char):
    __tablename__ = 'kanji'
    __mapper_args__ = {"polymorphic_identity": "kanji"}

    kanji_id = db.Column(None, db.ForeignKey('char.kao'), primary_key=True)
    radical = db.Column(db.String, nullable=True, default=None)
    hint = db.Column(db.String, nullable=True, default=None)
    onyomi = db.Column(db.String, nullable=True, default=None)
    kunyomi = db.Column(db.String, nullable=True, default=None)
    meanings = db.Column(db.String, nullable=True, default=None)


class Tsubu(db.Model):
    __tablename__ = "tsubu"
    __mapper_args__ = {"polymorphic_identity": "tsubu",
                       "polymorphic_on": "tsubu_type",
                       "with_polymorphic": "*"}
    id = db.Column(db.String, primary_key=True)
    tsubu_type = db.Column(db.String)
    imi = db.Column(db.String, default="")
    tosa_id = db.Column(db.String, db.ForeignKey('tsubu.id'))
    uchiryuu = db.relationship("Tsubu",
                               backref=db.backref("tosa", remote_side=[id]),
                               foreign_keys=[tosa_id])


class Ryuushi(Tsubu):
    __tablename__ = "ryuushi"
    __mapper_args__ = {"polymorphic_identity": "ryuushi"}

    ryuushi_id = db.Column(db.String, db.ForeignKey('tsubu.id'))
    char_kao = db.Column(db.String, db.ForeignKey('char.kao'))
    char = db.relationship("Char", foreign_keys=[char_kao])
    onsei = db.Column(db.String, default=None, nullable=True)
