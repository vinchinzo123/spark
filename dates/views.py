from django.shortcuts import render, reverse, HttpResponseRedirect
from dates.models import DatesNightModel
from dates.forms import ChooseDateCategory, CreateADiningDate, CreateAnEntertainmentDate, CreateAnOutdoorsDate, CreateAStayHomeDate, Preferences
from notifications.models import Notification


def create_a_date_view(request):
    if request.method == 'POST':
        form = ChooseDateCategory(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            date_category = data['choice']
            if date_category == 'Dining':
                return HttpResponseRedirect(reverse('dining'))
            elif date_category == 'Entertainment':
                return HttpResponseRedirect(reverse('entertainment'))
            elif date_category == 'Outdoors':
                return HttpResponseRedirect(reverse('outdoors'))
            elif date_category == 'Stay_At_Home':
                return HttpResponseRedirect(reverse('stayhome'))
    # prefered = Preferences.objects.all()
    # choice = prefered.get_choice_display()
    form = ChooseDateCategory()
    return render(request, 'form.html', {'form': form})


def dining_date(request):
    if request.method == 'POST':
        form = CreateADiningDate(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_date = DatesNightModel.objects.create(
                dining_category=data['dining_category'],
                users_one=request.user,
                users_two=data['users_two'],
                location=data['location'],
                when_data_time=data['when_date_time']
            )
            new_notification = Notification.objects.create(
                date_night=new_date,
                sent_user=request.user,
                received_user=data['users_two']
            )
            return HttpResponseRedirect(reverse('home'))
    form = CreateADiningDate()
    return render(request, 'form.html', {'form': form})
            

def entertainment_date(request):
    if request.method == 'POST':
        form = CreateAnEntertainmentDate(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_date = DatesNightModel.objects.create(
                entertainment_category=data['entertainment_category'],
                users_one=request.user,
                users_two=data['users_two'],
                location=data['location'],
                when_data_time=data['when_date_time']
            )
            new_notification = Notification.objects.create(
                date_night=new_date,
                sent_user=request.user,
                received_user=data['users_two']
            )
            return HttpResponseRedirect(reverse('home'))
    form = CreateAnEntertainmentDate()
    return render(request, 'form.html', {'form': form})
            

def outdoors_date(request):
    if request.method == 'POST':
        form = CreateAnOutdoorsDate(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_date = DatesNightModel.objects.create(
                out_doors_category=data['out_doors_category'],
                users_one=request.user,
                users_two=data['users_two'],
                location=data['location'],
                when_data_time=data['when_date_time']
            )
            new_notification = Notification.objects.create(
                date_night=new_date,
                sent_user=request.user,
                received_user=data['users_two']
            )
            return HttpResponseRedirect(reverse('home'))
    form = CreateAnOutdoorsDate()
    return render(request, 'form.html', {'form': form})
            

def stay_home_date(request):
    if request.method == 'POST':
        form = CreateAStayHomeDate(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_date = DatesNightModel.objects.create(
                stay_home_category=data['stay_home_category'],
                users_one=request.user,
                users_two=data['users_two'],
                location=data['location'],
                when_data_time=data['when_date_time']
            )
            new_notification = Notification.objects.create(
                date_night=new_date,
                sent_user=request.user,
                received_user=data['users_two']
            )
            return HttpResponseRedirect(reverse('home'))
    form = CreateAStayHomeDate()
    return render(request, 'form.html', {'form': form})
    
    