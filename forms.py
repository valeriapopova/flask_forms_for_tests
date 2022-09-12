from wtforms import Form, StringField, SelectField, IntegerField, SubmitField, RadioField
from wtforms.widgets import NumberInput


class MethodForm(Form):
    method = RadioField('method', choices=["GET", "POST"])
    submit = SubmitField('send method')


class RequestForm(Form):
    apiendpoint = StringField('apiendpoint')
    loop_count = IntegerField('loop_count', widget=NumberInput(min=1))
    number_of_threads = IntegerField('number_of_threads', widget=NumberInput(min=1))
    data = StringField('data')
    submit = SubmitField('Send')


class RequestGetForm(Form):
    apiendpoint = StringField('apiendpoint')
    loop_count = IntegerField('loop_count', widget=NumberInput(min=1))
    number_of_threads = IntegerField('number_of_threads', widget=NumberInput(min=1))
    submit = SubmitField('Send')