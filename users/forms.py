from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    display_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)

    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)