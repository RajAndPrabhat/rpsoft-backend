from django.db import models
from django.core.validators import RegexValidator

# Create your models here.t
class Lead(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$',
        message=(
            "Phone number must be entered in the format: +999999999"
            " Up to 14 digits allowed.")
    )

    SOURCE_CHOICES = (
        ('App', 'App'),
        ('Web', 'Web'),
    )


    name=models.CharField(max_length=25, blank=True)
    emai_id=models.EmailField(max_length=255, blank=True)
    phone=models.CharField(validators=[phone_regex], max_length=15,)
    message=models.TextField(max_length=500)
    source=models.CharField(max_length=20, choices=SOURCE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OurWork(models.Model):
    name=models.CharField(max_length=100)
    image=models.FileField(upload_to='clients/')
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Slider(models.Model):
    name=models.CharField(max_length=100)
    image=models.FileField(upload_to='sliders/')
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ClientReview(models.Model):
    client_name=models.CharField(max_length=100)
    review=models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OurService(models.Model):
    service_name=models.CharField(max_length=100)
    service_image=models.CharField(max_length=100)
    service_description=models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OurTech(models.Model):
    tech_name=models.CharField(max_length=100)
    tech_image=models.ImageField(upload_to='tech/')
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

