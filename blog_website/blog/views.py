from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import UserTable
def users(request):
    myusers = UserTable.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'myusers' : myusers,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())