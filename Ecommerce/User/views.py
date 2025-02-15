from django.shortcuts import render, get_object_or_404
from .models import *



# Create your views here.


def home(request):
    categories = category.objects.all()  # Use 'categories' instead of 'category'
    subcategories = [cat.subcategory_set.all() for cat in categories]
    sliders = slider.objects.all()[:3]
    products=product.objects.all()
    context = {
        'sliders': sliders,
        'subcategories': subcategories,
        'categories': categories,
        'products': products,  # Use 'products' instead of 'product'
    }
    return render(request, 'home.html', context)



def product_detail(request,pk,slug):
    products = get_object_or_404(product, id=pk, slug=slug)
    images = Additional_image.objects.filter(product=products)  # Assuming FK exists
    context={
        'products': products , # Use 'products' instead of 'product'
        'additional_images': images,
    }
    return render(request, 'product_details.html',context)
