from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

# choices(value, label)
class ShippingForm(FlaskForm):
    sender = StringField("Sender", validators=[DataRequired()])
    recipient = StringField("Recipient", validators=[DataRequired()])
    origin = SelectField('Origin', choices=[x for x in map], validators=[DataRequired()])
    destination = SelectField('Destination', choices=[x for x in map], validators=[DataRequired()])
    express_shipping = BooleanField("Express?")
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')
