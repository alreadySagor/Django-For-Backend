from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    # backend theke onek data ei template e amra pathai dite pari ba render korte pari
    # Seta hocche ekta dictionary format e
    # dictionary format e pathano lagbe (Dictionary er vitore list ba onno vabeu pathate pari)
    # seta dui vabe pass kora jay, 
    # 1... return render(request, "home.html", d)
    # 2... return render(request, "home.html", context = d)
    
    d = {'author': "Rahim", 'age': 6, 'lst' : ['python', 'is', 'best'],
        'birthday' : datetime.datetime.now(),
        'val' : '',
        'courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 10000
        },
        {
            'id' : 3,
            'name' : 'C',
            'fee' : 1000
        },
    ]}  # d ekti dictionary
    return render(request, "home.html", d) # context = d O dite pari, eki bepar