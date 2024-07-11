from django import forms

class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField(label='Password Length', min_value=4)
    count = forms.IntegerField(label='Number of Passwords', min_value=1)

