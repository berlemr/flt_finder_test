from flask_wtf import FlaskForm
from wtforms import DateField,StringField, PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    from_date = DateField('DatePicker', format='%Y-%m-%d')
    to_date = DateField('DatePicker', id='to_date-1')
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    autocomplete = StringField('autocomp', id='autocomplete', validators=[DataRequired()])

    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In', render_kw={"onclick": "$('#loading').show();"})