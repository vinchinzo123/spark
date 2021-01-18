from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from preferences.models import Entertainment, Dining, OutDoors, StayHome, Preferences
from preferences.forms import AddToCategoriesForm, AddToDiningForm, AddToEntertainmentForm, AddToOutDoorsForm, AddToStayHomeForm
from dates.forms import ChooseDateCategory
from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models

from django.views import View


class AddADateOptionView(LoginRequiredMixin, View):
    class_form = ChooseDateCategory
    template = 'generic_form.html'

    def get(self, request):
        form = self.class_form()
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = ChooseDateCategory(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            date_category = data["choice"]
            if date_category == "Entertainment":
                return HttpResponseRedirect(reverse("add_to_entertainment"))
            elif date_category == "Dining":
                return HttpResponseRedirect(reverse("add_to_dining"))
            elif date_category == "Outdoors":
                return HttpResponseRedirect(reverse("add_to_outdoors"))
            elif date_category == "Stay_Home":
                return HttpResponseRedirect(reverse("add_to_stayhome"))


class AddToCategoriesView(LoginRequiredMixin, View):
    class_form = AddToCategoriesForm
    template = 'generic_form.html'

    def get(self, request):
        form = self.class_form()
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_category = data['choice']
            new_preferences_category = Preferences.objects.create(
                choice=data['choice']
            )
            # new_model = self.create_model(new_category)
            return HttpResponseRedirect(reverse('homepage'))
        
    def create_model(self, new_category):
        choice_list = [
            ('', '-------')
        ]
        class Meta:
            app_label='preferences'
        
        def to_string(self):
            return f'{{new_category}}'
        
        fields = {
            'Meta': Meta,
            '__module__': 'preferences',
            '__str__': to_string,
            '__unicode__': to_string,
            'choice': models.CharField(max_length=50, choices=choice_list)
        }
        new_model = type(new_category, (models.Model,), fields)
        admin.site.register(new_model)
        return new_model


class HelperView(View):

    def get(self, request):
        form = self.class_form()
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_date_option = data['choice']
            new_option = self.obj.objects.create(
                choice=new_date_option
            )
            return HttpResponseRedirect(reverse('homepage'))  


class AddToEntertainmentOptionsView(LoginRequiredMixin, View):
    class_form = AddToEntertainmentForm
    obj = Entertainment
    template = 'generic_form.html'
    def get(self, request):
        return HelperView.get(self, request)
    
    def post(self, request):
        return HelperView.post(self, request)


class AddToDiningOptionsView(LoginRequiredMixin, View):
    class_form = AddToDiningForm
    obj = Dining
    template = 'generic_form.html'
    def get(self, request):
        return HelperView.get(self, request)
    
    def post(self, request):
        return HelperView.post(self, request)


class AddToOutdoorsOptionsView(LoginRequiredMixin, View):
    class_form = AddToOutDoorsForm
    obj = OutDoors
    template = 'generic_form.html'
    def get(self, request):
        return HelperView.get(self, request)
    
    def post(self, request):
        return HelperView.post(self, request)


class AddToStayHomeOptionsView(LoginRequiredMixin, View):
    class_form = AddToStayHomeForm
    obj = StayHome
    template = 'generic_form.html'
    def get(self, request):
        return HelperView.get(self, request)
    
    def post(self, request):
        return HelperView.post(self, request)