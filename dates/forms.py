from django import forms
from preferences.models import Preferences
from dates.models import DatesNightModel

class ChooseDateCategory(forms.ModelForm):
    
    class Meta:
        model = Preferences
        fields = ['choice']
    
    choice = forms.ModelChoiceField(queryset=Preferences.objects.all())


class CreateADiningDate(forms.ModelForm):
    class Meta:
        model = DatesNightModel
        fields = [
            'dining_category',
            'users_one',
            'users_two',
            'location',
            'when_date_time'
            ]


class CreateAnEntertainmentDate(forms.ModelForm):
    class Meta:
        model = DatesNightModel
        fields = [
            'entertainment_category',
            'users_one',
            'users_two',
            'location',
            'when_date_time'
            ]


class CreateAnOutdoorsDate(forms.ModelForm):
    class Meta:
        model = DatesNightModel
        fields = [
            'out_doors_category',
            'users_one',
            'users_two',
            'location',
            'when_date_time'
            ]


class CreateAStayHomeDate(forms.ModelForm):
    class Meta:
        model = DatesNightModel
        fields = [
            'stay_home_category',
            'users_one',
            'users_two',
            'location',
            'when_date_time'
            ]
