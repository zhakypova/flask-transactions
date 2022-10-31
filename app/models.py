from . import db


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    status = db.Column(db.String(30))
    unit = db.Column(db.String(30))
    comment = db.Column(db.String(50))

    def __repr__(self):
        return self.value
