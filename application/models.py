from django.db import models

class ServiceCybrom(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to='Service_images')
    desc=models.TextField()
    duration=models.CharField(max_length=40)

    def __str__(self):
        return self.name
       

class ServiceRelated(models.Model):
    service=models.OneToOneField(ServiceCybrom,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    full_desc=models.TextField()
    fees=models.FloatField()

    def __str__(self):
        return self.name


class ProjectCybrom(models.Model):
    image=models.ImageField(upload_to='Project_images')

class AboutCybrom(models.Model):
    heading=models.CharField(max_length=50)
    desc=models.CharField(max_length=150)
    quality=models.CharField(max_length=40)
    image=models.ImageField(upload_to='About_image')

class Contact_us(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    mobile_no=models.BigIntegerField()
    query=models.TextField()

class SectionSix(models.Model):
    desc=models.CharField(max_length=100)
    client_image=models.ImageField(upload_to="images_clients")
    client_name=models.CharField(max_length=40)
    profession=models.CharField(max_length=40)

class final(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    fees=models.BigIntegerField()
    query=models.TextField()

