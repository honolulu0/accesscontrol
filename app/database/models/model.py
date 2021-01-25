from ... import db

print ('user_db')


class AccessRecord(db.Model):
    __tablename__ = 'access_record'

    id = db.Column(db.Integer, primary_key=True)
    recordCardNO = db.Column(db.String(64))
    sn = db.Column(db.String(64))
    recordInOrOut = db.Column(db.String(64))
    recordValid = db.Column(db.String(64))
    recordType = db.Column(db.String(64))
    recordDoorNO = db.Column(db.String(64))
    recordIndex = db.Column(db.String(64))
    reason = db.Column(db.String(128))
    recordTime = db.Column(db.DateTime)


class ApplicationForm(db.Model):
    __tablename__ = 'application_form'

    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer)
    sn = db.Column(db.String(64))
    recordCardNO = db.Column(db.String(64))
    state = db.Column(db.Integer)
    times = db.Column(db.Integer)
    limit = db.Column(db.String(64))
    explain = db.Column(db.String(128))
    time = db.Column(db.DateTime)


class ControllerTable(db.Model):
    __tablename__ = 'controller_table'

    id = db.Column(db.Integer, primary_key=True)
    controllerId = db.Column(db.String(64))
    ip = db.Column(db.String(64))
    labId = db.Column(db.Integer)
    state = db.Column(db.Integer)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(64))
    itcode = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Integer)
    confirmed_at = db.Column(db.DateTime)
    api_key = db.Column(db.String(32))
    roleid = db.Column(db.Integer)
    usergroups = db.Column(db.String(32))
    display_name = db.Column(db.String(64))
    manager = db.Column(db.String(255))
    card_number = db.Column(db.String(64))
