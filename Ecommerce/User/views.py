from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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



def product_detail(request,pk,slug=None):      
    products = get_object_or_404(product, id=pk, slug=slug) if slug else get_object_or_404(product, id=pk)
    images = Additional_image.objects.filter(product=products)  # Assuming FK exists
    context={
        'products': products , # Use 'products' instead of 'product'
        'additional_images': images,
    }
    return render(request, 'product_details.html',context)

def shop(request):
    categories = category.objects.all()  # Use 'categories' instead of 'category'
    products=product.objects.all()
    context = {
        'categories': categories,
        'products': products,  # Use 'products' instead of 'product'
    }
    return render(request,'product_view.html',context)

def category_products(request, slug):
    category = get_object_or_404(category, slug=slug)
    products = product.objects.filter(category=category)  # Get products for selected category

    context = {
        'category': category,
        'products': products,
    }    


def filter_category(request):
    category_id = request.GET.get('category_id')
    
    if not category_id:
        return redirect("error_page")  # Redirect if category ID is missing

    try:
        products = Product.objects.filter(category_id=category_id).values('id', 'title', 'price', 'feature_image')

        if not products:
            return redirect("error_page")  # Redirect if no products found

        return JsonResponse(list(products), safe=False)

    except Exception as e:
        return redirect("error_page")  # Redirect on any error

def error_page(request, message="Something went wrong"):
    return render(request, "404.html", {"error": message}, status=404) 

def shop_page(request):
    categories = category.objects.all()
    products = product.objects.all()  # Load all products initially
    
    return render(request, 'shop.html', {'categories': categories, 'products': products})
