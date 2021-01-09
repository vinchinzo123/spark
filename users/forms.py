from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class UpdateProfileForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField( max_length=254)
    location = forms.CharField(max_length=50)
