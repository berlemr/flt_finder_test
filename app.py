import os
import time

from flask import Flask, render_template, flash, redirect, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

from forms import LoginForm

os.environ['APP_SETTINGS'] = 'config.DevelopmentConfig' #just for convenience, remove when finished development

app = Flask(__name__)
cfg = import_string(os.environ['APP_SETTINGS'])()
app.config.from_object(cfg)
db = SQLAlchemy(app)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), unique=True, nullable=False)

NAMES = [i.city for i in Destination.query.all()]

@app.route('/')
def index():
    return "this is the index"

@app.route('/test')
def test():
    return render_template('test.html', title='test')


@app.route('/autocomplete',methods=['GET'])
def autocomplete():
    search = request.args.get('term')
    app.logger.debug(search)
    return jsonify(json_list=NAMES)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # return render_template('index.html')
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        print('Login requested for user {}, remember_me={}, from={}, destination={}'.format(
            form.username.data, form.remember_me.data, form.from_date.data, form.autocomplete.data))
        time.sleep(20)
        return redirect('/')
    return render_template('form.html', title='Sign In', form=form)


if __name__ == '__main__':
    print(os.environ['APP_SETTINGS'])
    app.run()