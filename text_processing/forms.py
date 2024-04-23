from django import forms

class TextFileForm(forms.Form):
    text_file = forms.FileField(label='File')
