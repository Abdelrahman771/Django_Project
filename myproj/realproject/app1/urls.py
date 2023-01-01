from django.urls import path 
from . import views

urlpatterns = [
    path('',views.renderhtml),
    path('cars/' , views.viewCars , name ="viewCars"),
    path('createcar/' , views.createCar , name ="createCar"),
    path('showcar/<id>' , views.showCarWithID , name ="showCar"),
    path('deletecar/<id>' , views.deleteCarWithID , name ="deleteCar"),
    path('updatecar/<id>' , views.updateCarWithID , name ="updateCar")
]  
