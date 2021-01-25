# coding= utf-8
from .. import db


class Commons:
    def __init__(self):
        pass

    def add(self, *Obj):
        try:
            db.session.add_all(*Obj)
            db.session.commit()
            return 1
        except Exception as e:
            db.session.rollback()
            print(e)
            return e
