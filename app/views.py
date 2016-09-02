from django.shortcuts import render, redirect
from app.models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, logout,authenticate 
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import escape
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def location(request):
    context = {}

    


    