from .views import app, show_transactions, create_transac

app.add_url_rule('/', view_func=show_transactions, methods=['GET', ], endpoint='show_transactions')
app.add_url_rule('/create', view_func=create_transac, methods=['GET', 'POST'], endpoint='create_transac')