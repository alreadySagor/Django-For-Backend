from django.shortcuts import render
import datetime
def home(request):

    d = {
        'name_1' : "Sagor",
        'name_2' : "sagor ahmed",
        'name_3' : "sAgOr aHmEd",
        'name_4' : "my name is summy al ahmed sagor",
        'name_5' : "I'm sagor ahmed",
        'age' : 23,

        'lst' : ['python', 'for', 'backend'],
        'birthday' : datetime.datetime.now(),

        'val' : '',

        'courses' : [
            {
                'id' : 1,
                'name' : 'Python',
                'fee' : 4000,
            },
            {
                'id' : 2,
                'name' : 'Cpp',
                'fee' : 3700,
            },
            {
                'id' : 3,
                'name' : 'Data Structure',
                'fee' : 5500,
            }
        ],
        'lis' : [
            {'name' : "John", 'Age' : 53},
            {'name' : "Lara", 'Age' : 43},
            {'name' : "Alex", 'Age' : 27},
            {'name' : "William", 'Age' : 23},
            {'name' : "Laura", 'Age' : 15},
        ]
    }
    return render(request, 'home.html', d)