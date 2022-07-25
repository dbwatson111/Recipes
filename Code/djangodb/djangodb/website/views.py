from django.shortcuts import render
from .models import Member

def home(request):
    all_members = Member.objects.all #assigns everything in database into variable
    return render(request, 'home.html', {'all':all_members}) #passes all_members into all to be referenced in html page

def join(requests):
    return render(requests, 'join.html', {})

def index(requests):
    return render(requests, 'index.html', {})