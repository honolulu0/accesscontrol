# coding=utf-8

from flask import Blueprint, session, request

from .bean.resultBean import ResultBean
from .service import *
from ..database.apis import userApi

userRoute = Blueprint('userRoute', __name__)


@userRoute.route('/add', methods=['POST'])
def adduser():
    card_number = request.json.get('cardnumber')
    itcode = request.json.get('itcode')

    if userApi.add_cardnumber_by_user(itcode, card_number) == 1:
        session['itcode'] = itcode
        result = ResultBean().success()
    else:
        result = ResultBean().fail()
    return result


@userRoute.route('/addpermit', methods=['POST'])
def addpermit():
    res = add_permit()
    print(res)
    # if userApi.add_cardnumber_by_user(itcode, card_number) == 1:
    #     session['itcode'] = itcode
    #     result = ResultBean().success()
    # else:
    #     result = ResultBean().fail()
    return '1'
