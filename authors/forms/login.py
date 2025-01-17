from django import forms
from utils.django_forms import add_placeholder


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Digite o usuário')
        add_placeholder(self.fields['password'], 'Informe a senha')

    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
