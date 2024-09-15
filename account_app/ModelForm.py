from django import forms
from .models import Account



class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['id', 'name', 'email', 'password', 'image']
        widgets = {
            'password': forms.PasswordInput(),  # To ensure the password is hidden
        }
