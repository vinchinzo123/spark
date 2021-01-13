from django import forms
from preferences.models import Preferences, Dining, Entertainment, OutDoors, StayHome
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


class AppendDiningDate(forms.Form):
    dining_category = forms.ModelMultipleChoiceField(queryset=Dining.objects.all())


class CreateAnEntertainmentDate(forms.Form):
    entertainment_category = forms.ModelMultipleChoiceField(
        queryset=Entertainment.objects.all()
    )
    users_two = forms.ModelChoiceField(required=False, queryset=User.objects.all())
    location = forms.CharField()
    date_day = forms.CharField()
    date_time = forms.CharField()


class AppendEntertainmentDate(forms.Form):
    entertainment_category = forms.ModelMultipleChoiceField(
        queryset=Entertainment.objects.all()
    )


class CreateAnOutdoorsDate(forms.Form):
    out_doors_category = forms.ModelMultipleChoiceField(queryset=OutDoors.objects.all())
    users_two = forms.ModelChoiceField(required=False, queryset=User.objects.all())
    location = forms.CharField()
    date_day = forms.CharField()
    date_time = forms.CharField()


class AppendOutdoorDate(forms.Form):
    out_doors_category = forms.ModelMultipleChoiceField(queryset=OutDoors.objects.all())


class CreateAStayHomeDate(forms.Form):
    stay_home_category = forms.ModelMultipleChoiceField(queryset=StayHome.objects.all())
    users_two = forms.ModelChoiceField(required=False, queryset=User.objects.all())
    location = forms.CharField()
    date_day = forms.CharField()
    date_time = forms.CharField()


class AppendStayHomeDate(forms.Form):
    stay_home_category = forms.ModelMultipleChoiceField(queryset=StayHome.objects.all())
