from django import forms
from django.core.exceptions import ValidationError
from .utils import check_control_digit

class PeselField(forms.Field):
    def validate(self, value):
        length = len(str(value))
        if not value.isnumeric():
            raise ValidationError('PESEL number may only consist of digits')
        if length != 11:
            raise ValidationError(f'PESEL number must have 11 digits, you have {length}')
        if not check_control_digit(str(value)):
            raise ValidationError('PESEL number is incorrect')


class PeselForm(forms.Form):
    pesel_number = PeselField(
        label='PESEL',
    )
    
