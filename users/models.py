from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

class DomainForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=100)
    idea = models.CharField( max_length=200)
    location = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=10)

class Feedback(models.Model):
    RATING_CHOICES = [
        (5, 'Excellent'),
        (4, 'Very Good'),
        (3, 'Good'),
        (2, 'Fair'),
        (1, 'Poor'),
        (0, 'Very Poor')
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    feedback = models.TextField()

class Forum_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    ask = models.CharField(max_length=100)
    call = models.CharField(max_length=100)
    pro = models.CharField(max_length=100)
    res = models.CharField(max_length=100)


class Stack_details(models.Model):
    ROLS = [
        (6, 'MANAGER'),
        (5, 'HR'),
        (4, 'CFO'),
        (3, 'CTO'),
        (2, 'FOUNDER'),
        (1, 'CEO'), 
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    role = models.IntegerField(choices=ROLS , default=3)
    equity = models.CharField(max_length=100)
    invest = models.CharField(max_length=100)
    decision = models.CharField(max_length=100)
    involvement = models.CharField(max_length=100)
    interest = models.CharField(max_length=100)
    retunrs = models.CharField(max_length=100)
    exit_sta = models.CharField(max_length=100)