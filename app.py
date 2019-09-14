import os

from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

from forms import LoginForm


os.environ['APP_SETTINGS'] = 'config.DevelopmentConfig' #just for convenience, remove when finished development

app = Flask(__name__)
cfg = import_string(os.environ['APP_SETTINGS'])()
app.config.from_object(cfg)
db = SQLAlchemy(app)

from models import *

@app.route('/')
def index():
    return "this is the index"

@app.route('/login', methods=['GET', 'POST'])
def login():
    # return render_template('index.html')
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('form.html', title='Sign In', form=form)


if __name__ == '__main__':
    print(os.environ['APP_SETTINGS'])
    app.run()