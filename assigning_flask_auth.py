from flask import Flask, render_template
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'jdesselles'
app.config['BASIC_AUTH_PASSWORD'] = 'ThisIsAPasswordDontHackOKThxBby'

basic_auth = BasicAuth(app)

@app.route('/secret')
@basic_auth.required
def secret_view():
    return render_template('secret.html')