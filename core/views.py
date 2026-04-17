from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return HttpResponseRedirect(reverse('login'))
