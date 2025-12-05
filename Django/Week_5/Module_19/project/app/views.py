from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.http import HttpResponse
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

def set_session(request):
    data = {
        'name' : 'rahim',
        'age' : 23,
        'language' : 'Bangla',
    }
    # print(request.session.get_session_cookie_age()) # eta second er hisab kore (koto second por sesh hobe seta)
    # print(request.session.get_expiry_date()) # koto din por jinish ta sesh hobe seta dekhlam. (ar eta date show kore, kobe sesh hobe seta)
    # request.session.update(data)
    request.session['name'] = 'Karim'
    return render(request, 'home.html')

def get_session(request):
    if 'name' in request.session: # 10 seconds somoy dhore nam ta theke jabe then 10s por delete hoye gele else er moddhe dhuke else er kaj korbe
        name = request.session.get('name', 'Guest') # delete korar por nam na thakle Guest lekha ashbe (default vabe None thake)
        age = request.session.get('age')
        request.session.modified = True #
        return render(request, 'get_session.html', {'name': name, 'age' : age})
    else:
        return HttpResponse('Your session has been expired. Login again')
def delete_session(request):
    # del request.session['name'] # kono ekti data like name delete korte chaile
    
    request.session.flush() # sob kichu delete korte chaile
    return render(request, 'delete_session.html')
