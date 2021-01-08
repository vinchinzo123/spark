from django import forms
from preferences.models import Preferences, Dining
from dates.models import DatesNightModel
from users.models import User


class ChooseDateCategory(forms.ModelForm):
    class Meta:
        model = Preferences
        fields = ["choice"]


# class CreateADiningDate(forms.ModelForm):
#     class Meta:
#         model = DatesNightModel
#         fields = [
#             "dining_category",
#             "users_two",
#             "location",
#         ]
class CreateADiningDate(forms.Form):
    dining_category = forms.ModelMultipleChoiceField(queryset=Dining.objects.all())
    users_two = forms.ModelChoiceField(required=False, queryset=User.objects.all())
    location = forms.CharField()
    date_day = forms.CharField()
    date_time = forms.CharField()


class CreateAnEntertainmentDate(forms.ModelForm):
    class Meta:
        model = DatesNightModel
        fields = [
            "entertainment_category",
            "users_one",
            "users_two",
            "location",
            "when_date_time",
        ]


class CreateAnOutdoorsDate(forms.ModelForm):
    class Meta:
        model = DatesNightModel
        fields = [
            "out_doors_category",
            "users_one",
            "users_two",
            "location",
            "when_date_time",
        ]


class CreateAStayHomeDate(forms.ModelForm):
    class Meta:
        model = DatesNightModel
        fields = [
            "stay_home_category",
            "users_one",
            "users_two",
            "location",
            "when_date_time",
        ]
