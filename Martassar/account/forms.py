from . models import Account
from django import forms


class AccountModelForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'nama',
            'gender',
            'umur',
            'alamat',
            'password1',
            'password2',
        ]
