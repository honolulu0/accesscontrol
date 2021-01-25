# coding=utf-8
from flask import request, Blueprint
from app.routes.bean.resultBean import ResultBean

accessControlRoute = Blueprint('accessControlRoute', __name__)

'''
{
    "reason": "刷卡禁止通过: 没有权限",
    "recordTime": "2021-01-13 15:06:01",
    "recordInOrOut": "进门",
    "recordValid": "禁止",
    "recordType": "1", 刷卡
    "recordDoorNO": "1", 第一个门
    "sn": "125029221", Sn 号
    "recordIndex": "89",
    "recordCardNO": "19665490" 卡号
}
'''


@accessControlRoute.route('/pushmsg', methods=['POST'])
def push_msg():
    recordCardNO = request.json.get('recordCardNO')
    sn = request.json.get('sn')
    recordDoorNO = request.json.get('recordDoorNO')
    recordType = request.json.get('recordType')
    if recordType == '1' and recordDoorNO == '1' and sn == '125029221':
        print(recordCardNO)
        result = ResultBean().success()
    else:
        result = ResultBean().fail()

    return result
