from flask_wtf import FlaskForm
from wtforms import DateField,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    from_date = DateField('DatePicker', format='%Y-%m-%d')
    to_date = DateField('DatePicker', format='%Y-%m-%d')
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')