from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from preferences.models import Entertainment, Dining, OutDoors, StayHome, Preferences
from preferences.forms import AddToCategoriesForm, AddToDiningForm, AddToEntertainmentForm, AddToOutDoorsForm, AddToStayHomeForm
from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models

from django.views import View

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


class AddToStayHomeOptionsView(LoginRequiredMixin, View):
    class_form = AddToStayHomeForm
    template = 'generic_form.html'

    def get(self, request):
        form = self.class_form()
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_date_option = data['choice']
            new_stayHome = StayHome.objects.create(
                choice=new_date_option
            )
            for option in StayHome.objects.all():
                print(option)
            return HttpResponseRedirect(reverse('homepage'))

