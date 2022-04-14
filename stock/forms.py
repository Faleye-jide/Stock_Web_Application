from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from . models import stock
from django.forms import ModelForm

class TickerForm(forms.Form):
    ticker = forms.CharField(label='Ticker', max_length=5)
    
    class Meta:
        model = stock
        fields = ['ticker']
        


class NewUserForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30)
    email = forms.EmailField(required=True, help_text='Enter a valid email address')

    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
        
    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=True)
    #     user.first_name=self.cleaned_data.get("first_name")
    #     user.last_name=self.cleaned_data.get("last_name")
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user 
    
    