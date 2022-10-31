from flask import request, render_template, redirect, url_for, flash

from . import app, db
from .models import Transactions
from .forms import TransactionsForm


def show_transactions():
    title = 'список всех транзакций'
    transactions = Transactions.query.all()
    return render_template('show_transactions.html', title=title, transactions=transactions)


def create_transac():
    title = 'добавление новой транзакции'
    form = TransactionsForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            transaction = Transactions()
            form.populate_obj(transaction)
            db.session.add(transaction)
            db.session.commit()
            flash(f'транзакция №{transaction.id} успешно добавлена', 'success')
            return redirect(url_for('show_transactions'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'ошибка в поле "{field}", текст ошибки: {error}', 'danger')
    return render_template('create_transaction.html', form=form, title=title)
