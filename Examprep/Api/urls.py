from django.contrib import admin
from django.urls import path
from Api import views

urlpatterns = [
    # urls for breed
    path('breeds/', views.BreedList.as_view(), name='breed-list'),
    path('breeds/<int:pk>/', views.BreedDetail.as_view(), name='breed-detail'),
    
    # urls for dog
    path('dogs/', views.DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', views.DogDetail.as_view(), name='dog-detail'),
    
    
]
