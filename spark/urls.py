"""spark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),

    path('delete_profile/<int:profile_id>/', views.delete_profile_view, name='delete_profile'),
    path('update_profile/<int:profile_id>/', views.update_profile_view, name='update_profile'),

    path('profile/<int:profile_id>/', views.profile_view, name='profile'),
    path('create_a_date/', views.create_a_date_view, name='create_a_date'),
    path('preferences/', views.preferences_view, name='preferences'),
    path('pending_dates/', views.pending_dates_view, name='pending_dates'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up_page')  

]
