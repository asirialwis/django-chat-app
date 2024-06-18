from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
  {'id':1 , 'name':'Lets Learn Python'},
  {'id':1 , 'name':'Design with'},
  {'id':1 , 'name':'Front end Python'},
]


def home(request):
  context = {'rooms':rooms}
  return render(request, 'base/home.html' , context)

def room(request):
  return render(request,'room.html')