from wtforms import Form, StringField, SelectField, IntegerField, SubmitField, RadioField
from wtforms.widgets import NumberInput


class MethodForm(Form):
    method = RadioField('method', choices=["GET", "POST"])
    submit = SubmitField('send method')


class RequestForm(Form):
    apiendpoint = StringField('ApiEndpoint')
    loop_count = IntegerField('Loop count', widget=NumberInput(min=1))
    number_of_threads = IntegerField('Number of threads', widget=NumberInput(min=1))
    master_product_id = IntegerField('master_product_id', widget=NumberInput(min=1))
    links = StringField('Links')
    submit = SubmitField('Send')


class RequestGetForm(Form):
    apiendpoint = StringField('ApiEndpoint')
    loop_count = IntegerField('Loop count', widget=NumberInput(min=1))
    number_of_threads = IntegerField('Number of threads', widget=NumberInput(min=1))
    submit = SubmitField('Send')