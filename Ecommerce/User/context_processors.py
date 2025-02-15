from .models import *  # Import your Category model

def categories(request):
    return {
        'categories': category.objects.all()  # Get all categories (modify as per your requirement)
    }