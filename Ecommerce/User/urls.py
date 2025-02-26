from django.urls import path,re_path

from . import views



urlpatterns = [
    path('', views.home,name='home'),
    re_path(r'^product_detail/(?P<pk>\d+)(?:/(?P<slug>[-a-zA-Z0-9_]+))?/$',views.product_detail, name='product_detail'),
    path('shop/',views.shop, name='shop'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('filter_category/',views.filter_category, name='filter_category'),
    path('shop/',views.shop_page, name='shop'),
    path('error_page/',views.error_page, name='error_page'),

]