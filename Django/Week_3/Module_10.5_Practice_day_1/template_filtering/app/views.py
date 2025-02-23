from django.shortcuts import render
import datetime
# Create your views here.
def home(request):

    d = {
        'Name' : "I'm sagor ahmed",
        'Name_2' : "sagor ahmed",
        'Name_3' : "sAgOr aHmEd",
        'Name_4' : "my name is summy al ahmed sagor",
        'Age' : 20,

        'Date__Time' : datetime.datetime.now(),

        'Str' : "",

        'lis' : [
            {'name' : "Dulal", 'Age' : 55},
            {'name' : "Samsunnaher", 'Age' : 43},
            {'name' : "Salim", 'Age' : 27},
            {'name' : "Sagor", 'Age' : 23},
            {'name' : "Dola", 'Age' : 15},
        ]

    }



    return render(request, "app/home.html", d)