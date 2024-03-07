
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


def admin(request):
    return HttpResponseRedirect(reverse('admin:index'))


def home(request):
    return render(request, 'hosted/home.html')
