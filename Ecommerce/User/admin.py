from django.contrib import admin
from .models import *



class subcategory(admin.TabularInline):
    model = subcategory

class categoryAdmin(admin.ModelAdmin):
    inlines = [subcategory]  

class AdditionalImageTabular(admin.TabularInline):
    model = Additional_image

class productAdmin(admin.ModelAdmin):
    inlines = [AdditionalImageTabular]

# Register your models here.

admin.site.register(slider)
admin.site.register(category,categoryAdmin)
admin.site.register(product,productAdmin)