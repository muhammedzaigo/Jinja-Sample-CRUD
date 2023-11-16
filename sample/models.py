from .utils import ACTIVE
from django.db import models
import uuid

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    name = models.CharField(max_length=256)
    description     =   models.TextField(blank=True,null=True)
    created_at    =   models.DateTimeField(auto_now_add=True)
    updated_at   =   models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='category_user')
    status   =   models.CharField(max_length=255,default=ACTIVE)    
        
    def __str__(self):                           
        return self.name



class Product(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True, blank=True,related_name='product_category')
    name = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True,upload_to='products/')
    description     =   models.TextField(blank=True,null=True)
    created_at    =   models.DateTimeField(auto_now_add=True)
    updated_at   =   models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='product_user')
    status   =   models.CharField(max_length=255,default=ACTIVE)    
        
    def __str__(self):                           
        return self.name

