from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Workflow Type', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('', validators=[DataRequired(), Email()])
    message = StringField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send')
