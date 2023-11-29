from django import forms


class SimpleLoginForm(forms.Form):
    username = forms.CharField(max_length=100)

