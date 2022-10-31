from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, \
    SubmitField, validators, ValidationError

from .models import Transactions


class TransactionsForm(FlaskForm):
    value = IntegerField(label='сумма транзакций', validators=[validators.DataRequired()])
    status = StringField(label='статус', validators=[validators.DataRequired()])
    unit = StringField(label='валюта', validators=[validators.DataRequired()])
    comment = StringField(label='комментарий', validators=[validators.DataRequired()])
    submit = SubmitField(label='save')

    def validate_value(self, value):
        if value.data is None:
            raise ValidationError('поле обязательно к заполнению')

    def validate_status(self, status):
        if status.data is None:
            raise ValidationError('поле обязательно к заполнению')

    def validate_unit(self, unit):
        if unit.data is None:
            raise ValidationError('поле обязательно к заполнению')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = []
        for transaction in Transactions.query.all():
            result.append((transaction.id, transaction.value))
        # self.transaction_id.choices = result
