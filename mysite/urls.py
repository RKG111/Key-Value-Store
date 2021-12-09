from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    
    path('get',views.get_data, name="get_all"),             #to get all the pairs of KEY VALUE PAIR
    path('get/key', views.get_value,name="get_value"),      #to get the VALUE of a particular KEY
    path('set/key', views.set_value, name ="set_value"),    #to set the VALUE of a particular KEY
]
