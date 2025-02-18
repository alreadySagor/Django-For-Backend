from django.shortcuts import render
import datetime
# Create your views here.
def about(request):
    return render(request, "navigation/about.html")

def contact(request):
    d = {
        'name' : 'Sagor Ahmed',
        'phone' : '+8801302436808',
        'address' : "25 Mail, Madhupur, Tangail, Dhaka, Bangladesh",
        'Date' : datetime.datetime.now(),
    }
    return render(request, "navigation/contact.html", d)