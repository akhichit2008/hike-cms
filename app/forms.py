from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    hike_uname = StringField('Hike Username',validators=[DataRequired])
    password = PasswordField('Password',validators=[DataRequired])