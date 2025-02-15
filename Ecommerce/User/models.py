from django.db import models
from ckeditor.fields import RichTextField
# from django.db.models import signals
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

# Create your models here.

# slider model creation
class slider(models.Model):
    CHOICES = (
        ('New Deal', 'New Deal'),
        ('New Arrivals', 'New Arrivals'),      
        ('Hot Deals', 'Hot Deals'),
        ('Best Seller', 'Best Seller'),

    )
    title = models.CharField(max_length=255)
    image=models.ImageField(upload_to='slider/')
    deal=models.CharField(choices=CHOICES,max_length=255)
    discount=models.PositiveBigIntegerField(default=0,null=True)

    def __str__(self):
        return self.title[:50]

# main category model creaton
class category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) ->str:
        return self.title[:50]  

# subcategory model creation
class subcategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
       return self.title[:50]              

# Product model creation
class product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(category, on_delete=models.DO_NOTHING)
    price=models.PositiveIntegerField(default=0,null=True)
    discount=models.PositiveIntegerField(default=0,null=True)
    feature_image=models.CharField(max_length=255,null=True) 
    brand=models.CharField(max_length=255,null=True)
    total=models.PositiveIntegerField(default=0,null=True)
    available=models.PositiveIntegerField(default=0,null=True)
    short_description=RichTextField(null=True, blank=True)
    description=RichTextField(null=True, blank=True)
    product_code=models.CharField(max_length=255,null=True, blank=True)
    tags=models.CharField(max_length=255,null=True,blank=True)
    slug=models.CharField(max_length=555,null=True,blank=True)

    def __str__(self):
        return self.title[:50]

@receiver(pre_save,sender=product)
def generate_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        base_slug=slugify(instance.title)
        unique_slug=base_slug

        while product.objects.filter(slug=unique_slug).exists():
            unique_slug=f"{base_slug}-{instance.id}"
        instance.slug=unique_slug


class Additional_image(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    image=models.CharField(max_length=555,null=True, blank=True)

