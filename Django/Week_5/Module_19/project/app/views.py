from django.shortcuts import render, redirect
from datetime import datetime, timedelta
# Create your views here.
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'rahim')
    # response.set_cookie('name', 'karim', max_age=10) # max_age = 10 mane holo 10 seconds por cookie delete hoye jabe
    response.set_cookie('name', 'karim', expires=datetime.utcnow()+timedelta(days=7)) # er mane holo name = karim 7 din er jonno ekhane set kora thakbe ar 7 din por eta delete hoye jabe
    return response

def get_cookie(request):
    name = request.COOKIES.get('name') # COOKIE ta dictionary format e ache/thake
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name' : name})

def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response