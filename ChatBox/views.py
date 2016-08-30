from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from chat import models





def home(request):
    """main page"""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('chat:chat'))
    else:
        return HttpResponseRedirect(reverse('chat:login'))