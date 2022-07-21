from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [

path('viewCars/',views.list_of_cars,name="listOfCars"),
path('addCars/',views.add_of_cars,name="addOfCars"),
path('deleteCars/',views.delete_of_cars,name="deleteOfCars"),    
    
]