from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from .forms import Carform
from django.template import RequestContext
# Create your views here.
users=[{"Name":"Abdelrahman","Age":"24","salary":"6000"}
            ,{"Name":"Ahmed","Age":"23","salary":"8000"}
            ,{"Name":"Ali","Age":"23","salary":"7000"}]
dict={"Data":users}
def renderhtml(request):
    return render(request, 'app1/index.html',dict)

def viewCars(request):
   
    return render(request,'app1/cars.html', {"cars":Car.objects.all()})

def createCar(request):
    car = Carform(request.POST , request.FILES)
    if car.is_valid():
        car.save()
    else:
        print("not valid")
    return render ( request , 'app1/createCar.html' , {"form":Carform})

def showCarWithID(request,id):
    car=Car.objects.get(pk=id)
    # print(car)
    return render(request, 'app1/carcards.html',{"car":car})

def deleteCarWithID(request,id):
    car=Car.objects.get(pk=id)
    car.delete()
    return render (request, 'app1/cars.html',{"cars":Car.objects.all()})

def updateCarWithID(request,id):
    car=Car.objects.get(pk=id)
    form = Carform(request.POST or None , request.FILES or None , instance=car  )
    if form.is_valid():
        form.save()
    else:
        print("not valid")
    return render(request, 'app1/updatecar.html',{"car":car,"form":form}) 