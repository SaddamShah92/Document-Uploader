from django.shortcuts import render
from django.http import HttpResponse

def home(request):
 peoples = [
    {'name': 'Arjun' , 'age': '25'},
    {'name': 'saddam' , 'age': '23'},
    {'name': 'muqeem' , 'age': '27'},
    {'name': 'ali' , 'age': '28'},
    {'name': 'sajawal', 'age': '21'}
 ]     
 vegtables = ['Tomato', 'Potato', 'Onion']
 
 return render(request, 'index.html', context= {'page': 'Home Page' ,'peoples' : peoples, 'vegtables' : vegtables} )

 

def contact(request):
 context = {'page': 'Contact Page' }
 return render(request, 'contact.html', context ) 

def about(request):
 context = {'page': 'About Page' }
 return render(request, 'about.html', context )

def success_page(request):
 return HttpResponse("<h1> This is a success page </h1>")