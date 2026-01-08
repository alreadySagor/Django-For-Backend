from django.shortcuts import render
import datetime
# Create your views here.
def index(request):

    d = {
        'Programmer' : 'Sagor Ahmed',
        'Age' : 16,
        'Blood_Group' : 'O-(Negative)',

        'list' : ['Python', 'is', 'best'],

        'value' : '',

        'Date' : datetime.datetime.now(),
        'courses' : [
            {
                'id' : 1,
                'name' : 'C',
                'fee' : 2000
            },
            {
                'id' : 2,
                'name' : 'C++',
                'fee' : 1500
            },
            {
                'id' : 3,
                'name' : 'Data Structure & Algorithm',
                'fee' : 3000
            },
        ]
    }
    return render(request,"app/index.html", context=d) # shudhu d likhleu cholto