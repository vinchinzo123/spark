from django import forms
from preferences.models import Preferences, Entertainment, Dining, OutDoors, StayHome


class AddToCategoriesForm(forms.Form):
    choice = forms.CharField(max_length=50, required=True)


class AddToEntertainmentForm(forms.Form):
    choice = forms.CharField(max_length=50, required=True)


class AddToDiningForm(forms.Form):
    choice = forms.CharField(max_length=50, required=True)


class AddToOutDoorsForm(forms.Form):
    choice = forms.CharField(max_length=50, required=True)


class AddToStayHomeForm(forms.Form):
    choice = forms.CharField(max_length=50, required=True)