from django.urls import path
from . import views



urlpatterns = [
    path('', views.home,name='home'),
    path('product_detail/<int:pk>/<slug:slug>/',views.product_detail, name='product_detail'),

]