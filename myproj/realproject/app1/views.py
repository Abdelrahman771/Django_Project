from django.shortcuts import render
from django.http import HttpResponse
from .models import Donation
from .forms import Donationform
from django.template import RequestContext
# Create your views here.

def renderhtml(request):
    return render(request, 'app1/index.html')

def viewDonation(request):
    return render(request,'app1/cars.html', {"cars":Donation.objects.all()})

def createDonation(request):
    donation = Donationform(request.POST , request.FILES)
    if donation.is_valid():
        donation.save()
    else:
        print("not valid")
    return render ( request , 'app1/createCar.html' , {"form":Donationform})

def showDonationWithID(request,id):
    donation=Donation.objects.get(pk=id)
    # print(car)
    return render(request, 'app1/carcards.html',{"donation":donation})

def deleteDonationWithID(request,id):
    donation=Donation.objects.get(pk=id)
    donation.delete()
    return render (request, 'app1/cars.html',{"cars":Donation.objects.all()})

def updateDonationWithID(request,id):
    donation=Donation.objects.get(pk=id)
    form = Donationform(request.POST or None , request.FILES or None , instance=donation  )
    if form.is_valid():
        form.save()
    else:
        print("not valid")
    return render(request, 'app1/updatecar.html',{"donation":donation,"form":form}) 