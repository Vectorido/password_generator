from django.shortcuts import render
import random
import string


# from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = string.ascii_lowercase
    if request.GET.get('uppercase'):
        characters = string.ascii_letters
    if request.GET.get('numbers'):
        characters += string.digits
    if request.GET.get('special'):
        characters += string.punctuation
    length = int(request.GET.get('length'))
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})


def describe_site(request):
    return render(request, 'generator/description.html')
