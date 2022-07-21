from django.shortcuts import render,redirect
from . import models
from django.urls import reverse

def list_of_cars(req):
    all_cars = models.Car.objects.all()
    return render(req,'cars/list.html',context={"all_cars":all_cars})

def add_of_cars(req):
    
    if req.POST:
        brand = req.POST['brand']
        year = int(req.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse('cars:listOfCars'))
    else:
        return render(req,'cars/add.html')

def delete_of_cars(req):
    if req.POST:
        pk = req.POST['pk']
        models.Car.objects.get(pk=pk).delete()
        return redirect(reverse('cars:listOfCars'))
    else:
        return render(req,'cars/delete.html')    
    