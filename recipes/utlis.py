from django.contrib import messages
from django.core.exceptions import ValidationError

valid_money = ['doler', 'AF', 'PK', 'ddaljdlajl']

def validator_money_from(value):
    if value not in valid_money:
        return ValidationError(f'value is not valid please enter valid meney')



