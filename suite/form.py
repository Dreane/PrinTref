from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired

class SendForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()], render_kw={'placeholder':'Имя'})
    room = StringField("Room: ", validators=[DataRequired()], render_kw={'placeholder':'Имя'})
    file = FileField("File:")
    submit = SubmitField("Submit")