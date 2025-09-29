from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    d = { # This is a Dictionary
        'author' : 'Rahim',
        'age' : 20,
        'lst' : ['python', 'is', 'best'], # This is a List
        'birthday' : datetime.datetime.now(),
        'val' : '',
        'courses' : [
            {
                'id' : 1,
                'name' : 'Python',
                'fee' : 5000,
            },
            {
                'id' : 2,
                'name' : 'Django',
                'fee' : 10500,
            },
            {
                'id' : 3,
                'name' : 'C++',
                'fee' : 3500,
            }
        ]
    }
    return render(request, 'app/index.html', d) # context = d