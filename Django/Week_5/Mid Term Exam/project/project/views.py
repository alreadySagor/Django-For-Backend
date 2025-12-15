from django.shortcuts import render, redirect
from brand.models import Brand
from car.models import Car

def home(request, brand_slug = None):
    data = Car.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        data = Car.objects.filter(brand = brand)
    brand = Brand.objects.all()
    return render(request, 'home.html', {'data' : data, 'brand' : brand})