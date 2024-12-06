from datetime import timezone

from django.db import models
from django.contrib.auth.models import User  # Assuming landlords are users in your system


class ContactInquiry1(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    agent_name = models.CharField(max_length=100)  # Field for storing selected agent's name


    def __str__(self):
        return self.name


class Contact1(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name


class Apartments1(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    bedrooms = models.IntegerField(default=1)
    description = models.TextField()
    image = models.ImageField(upload_to='apartment_images/')


    def __str__(self):
        return self.name

class Appartment1(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='apartments/')


    def __str__(self):
        return self.name

class UserProfile1(models.Model):
    # Name Fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)

    # Address Field
    address = models.TextField()

    # Gender Field
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    # Contact Fields
    phone_number = models.CharField(max_length=15)  # Depending on your phone number format, adjust max_length
    national_id_number = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"