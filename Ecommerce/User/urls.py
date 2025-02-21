from django.urls import path
from . import views



urlpatterns = [
    path('', views.home,name='home'),
    path('product_detail/<int:pk>/<slug:slug>/',views.product_detail, name='product_detail'),
<<<<<<< HEAD
=======
    path('shop/',views.shop, name='shop'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),


>>>>>>> 3d2669df (second commit)

]