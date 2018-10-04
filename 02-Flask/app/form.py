from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField,IntegerField, validators, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField




class QuestionForm(FlaskForm):
    
    titre = TextAreaField('Indicate the title', validators=[Length(min=0, max=100)])
    question = TextAreaField('Enter your question', validators=[Length(min=0, max=500)])
    

    submit = SubmitField('Send Question')
    
    

