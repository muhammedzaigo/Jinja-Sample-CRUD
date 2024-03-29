from django.urls import path

app_name = 'sample'

from .views import *

urlpatterns = [
    path('', LandingPage.as_view(),name='products'),
    path('product/add/', add_product, name='add_product'),
    path('product/edit/<uuid:prod_id>/', UpdateProduct.as_view(), name='edit_product'),
    path('product/delete/<uuid:prod_id>/', delete_product, name='delete_product'),
    
    path('categories/', categories,name='categories'),
    path('categories/<uuid:category_id>/', edit_categories,name='edit_categories'),

    
    
]