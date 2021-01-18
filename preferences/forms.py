from django import forms
from preferences.models import Preferences, Entertainment, Dining, OutDoors, StayHome


class AddToCategoriesForm(forms.Form):
    choice = forms.CharField(max_length=50, required=True)
    # class Meta:
    #     model=Preferences
    #     fields=['choice']


class AddToStayHomeForm(forms.Form):
    choice = forms.CharField(max_length=50, required=True)
    # class Meta:
    #     model=StayHome
    #     fields=['choice']


class AddToOutDoorsForm(forms.ModelForm):
    class Meta:
        model=OutDoors
        fields=['choice']


class AddToDiningForm(forms.ModelForm):
    class Meta:
        model=Dining
        fields=['choice']


class AddToEntertainmentForm(forms.ModelForm):
    class Meta:
        model=Entertainment
        fields=['choice']






# the code below was found at : https://stackoverflow.com/questions/24783275/django-form-with-choices-but-also-with-freetext-option
class ListTextWidget(forms.TextInput):
    def __init__(self, data_list, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list':'list__%s' % self._name})

    def render(self, name, value, attrs=None, renderer=None):
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list__%s">' % self._name
        for item in self._list:
            data_list += '<option value="%s">' % item
        data_list += '</datalist>'

        return (text_html + data_list)

class FormForm(forms.Form):
   char_field_with_list = forms.CharField(required=True)

   def __init__(self, *args, **kwargs):
        _country_list = kwargs.pop('data_list', None)
        super(FormForm, self).__init__(*args, **kwargs)
        self.fields['char_field_with_list'].widget = ListTextWidget(data_list=_country_list, name='country-list')
    # the "name" parameter will allow you to use the same widget more than once in the same
    # form, not setting this parameter differently will cuse all inputs display the
    # same list.