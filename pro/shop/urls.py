from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
   path('', views.indexshop, name="ShopeHome" ),
   path('about/', views.about, name="About" ),
   path('contact/', views.contact, name="Contact" ),
   path('tracker/', views.tracker, name="Tracker" ),
   path('products/<int:myid>', views.productview, name="Productview" ),
   path('search/', views.search, name="Search" ),
   path('checkout/', views.checkout, name="Checkout" ),
   path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
