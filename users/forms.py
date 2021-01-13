from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    display_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=200)
    location = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class UpdateProfileForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField( max_length=254)
    location = forms.CharField(max_length=50)

class ImageForm(forms.Form):
    picture = forms.ImageField()