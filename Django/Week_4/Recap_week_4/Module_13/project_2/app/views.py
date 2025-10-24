from django.shortcuts import render
import datetime
# Create your views here.
def movies(request):
    return render(request, './app/movies.html')

def submitForm(request):
    return render(request, './app/submit.html')

def seeReview(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        review = request.POST.get('review')
        rating = request.POST.get('select')
        time = datetime.datetime.now()

        verdict = ""
        if int(request.POST.get('select')) >= 3 and int(request.POST.get('select')) <= 5:
            verdict = "Good"
        elif int(request.POST.get('select')) >= 1 and int(request.POST.get('select')) < 2:
            verdict = "Poor"
        else:
            verdict = "Average"
        return render(request, './app/see.html', {'name' : name, 'email' : email, 'review' : review, 'rating' : rating, 'time' : time, 'verdict' :verdict})
    else:    
        return render(request, './app/see.html')