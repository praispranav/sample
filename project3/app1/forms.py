from django.forms import ModelForm
from .models import userlogin1
from django import forms

class userlogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = userlogin1
        fields = ['username','password']
