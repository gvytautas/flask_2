"""
-url_for
-flask-wtf
-CSRF (Cross-Site-Request-Forgery)
"""
from flask import Flask, render_template, request, redirect, url_for
from forms import AddClientForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "?``§=)()%``ÄLÖkhKLWDO=?)(_:;LKADHJATZQERZRuzeru3rkjsdfLJFÖSJ"

clients = []


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    form = AddClientForm()
    if request.method == 'POST':
        name = form.name.data
        clients.append({'name': name})
        return redirect(url_for('show_clients'))
    return render_template('add_client.html', form=form)


@app.route('/clients')
def show_clients():
    return render_template('clients.html', data=clients)


if __name__ == '__main__':
    app.run(debug=True)
