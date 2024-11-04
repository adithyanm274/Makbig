from django.db import models
 


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)  # Make sure this matches what you are trying to use
    mark = models.IntegerField()
    image = models.ImageField(upload_to='images/',blank=True,null=True,default='images/image.png')  # Ensure this field exists and matches the name used in your view

