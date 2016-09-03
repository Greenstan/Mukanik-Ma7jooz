from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserLoginForm
from app.models import CustomUser, CustomUserManager

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from datetime import datetime, timedelta, time 
from itertools import groupby
from app.models import Timeslot, location_model



import sys
import os
import glob
import json


# from simpleodspy.sodsspreadsheet import SodsSpreadSheet
# from simpleodspy.sodsods import SodsOds

# import csv



# Create your views here.


def timeslots(request):

    context = {}

    context['time_slots'] = Timeslot.objects.all()

 
    available_time = [
                  {'day': 'mon', 'time': '8:00', 'price': 0.150},
                  {'day': 'tue', 'time': '9:45', 'price': 0.150},
                  {'day': 'wed', 'time': '11:30', 'price': 0.150},
                  {'day': 'thu', 'time': '14:0', 'price': 0.150},
                  {'day': 'fri', 'time': '15:45', 'price': 0.150},
                  {'day': 'sat', 'time': '17: 30', 'price': 0.150}
                  ]

    for a_dict in available_time:
        for k, v in a_dict.items():
            print "key -- %s --- value %s" % (k,v)

    print available_time


    context['available_time'] = available_time
    
    return render(request, 'timeslots.html', context)


def order_confirmation(request): 

    context = {}

    return render(request, 'order_confirmation.html', context)

### not sure if def_key works!!!

def get_key(d):

    d = datetime.now()
    
    data = [d + timedelta(minutes=i) for i in xrange(100)]

    # prepare and group the data

    # group by 30 minutes
    
    k = d + timedelta(minutes=-(d.minute % 30)) 

    return datetime(k.year, k.month, k.day, k.hour, k.minute, 0)

    g = groupby(sorted(data), key=get_key)

# print data
    for key, items in g:
        
        print key


    for item in items:
        
        print '-', item


# Create your views here.

def homepage(request):

    context = {}

    return render (request, 'homepage.html', context)


def login_view(request):  
    context = {}

    context['form'] = CustomUserLoginForm()

    if request.method == 'POST':

        form = CustomUserLoginForm(request.POST)
        context['form'] = form

        if form.is_valid():
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password', None)

            auth_user = authenticate(username=email, password=password)

            try:
                login(request, auth_user)
            except Exception, e:
                message = """
                username or password incorrect, try again
                <a href='/login/'>login<a>
                """
                return HttpResponse(message)

    return render(request, 'signin.html', context)


def sign_up(request):

    context = {}

    context['form'] = CustomUserCreationForm()

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password1', None)

            auth_user = authenticate(username=email, password=password)

            try:
                login(request, auth_user)
            except Exception, e:
                print e
                return HttpResponse('invalid user or password, try again <a href="/signup/">here</a>')
            return redirect("/homepage")
    return render(request, 'signup.html', context)



def logout_view(request):  
    logout(request)

    return redirect('/signup/')

# Create your views here.


    


    