from typing import Optional
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class TickerForm(forms.Form):
    ticker = forms.CharField(label='Ticker', max_length=5)
    

class NewUserForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user 