
from ..models.model import *


def add_user(*user):
    e = Commons().add(*user)
    if e == 1:
        return 1
    else:
        return e


def add_cardnumber_by_user(user, cardnumber):
    try:
        db.session.query(User).filter(User.itcode == user).update({"card_number": cardnumber})
        db.session.commit()
        return 1
    except Exception as e:
        db.session.rollback()
        print(e)
        return e
