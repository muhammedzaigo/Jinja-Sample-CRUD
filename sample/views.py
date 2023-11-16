from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.
from django.views.generic.list import ListView

from .utils import ACTIVE, DELETE
from .models import *


class LandingPage(ListView):
    template_name = "product/product.html"
    context_object_name = 'products'
    model = Product
    
    def get_queryset(self) :
        return self.model.objects.filter(status=ACTIVE)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(status=ACTIVE)
        return context
    

  
def add_product(request, **kwargs):
    try:
        category_id = request.POST.get('add_category', None)
        category= Category.objects.filter(id=category_id).first()
        if not category:
            return JsonResponse({'status':False,'msg':"Category not found"})
        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        image = request.FILES.get('image')
        Product.objects.create(
            name = name, description = description, category=category,image=image
        )
        products = Product.objects.filter(status=ACTIVE)
        template=render_to_string('product/product_list.html',{'products': products})
        return JsonResponse({'status':True,"msg":"Product add Succesfully",'template':template})
    except Exception as e:
        return JsonResponse({'status':False, "msg" : str(e)}) 


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class UpdateProduct(APIView):

    def put(self, request, prod_id):
        try:
            product = Product.objects.filter(id=prod_id).first()
            if not product:
                return Response({'msg': "Product not found"}, status=status.HTTP_400_BAD_REQUEST)
            category_id = request.POST.get('edit_category', None)
            category= Category.objects.filter(id=category_id).first()
            if not category:
                return Response({'msg': "Category not found"}, status=status.HTTP_400_BAD_REQUEST)
            name = request.POST.get('edit_name', None)
            description = request.POST.get('edit_description', None)
            image = request.FILES.get('edit_image')
            product.name = name
            product.category = category
            product.description = description
            product.image = image
            product.save()
            return Response({'msg': 'Edit Success fully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_200_OK)
        
    

def delete_product(request, prod_id):
    try:
        product = Product.objects.filter(id=prod_id).first()
        if not product:
            return Response({'msg': "Product not found"}, status=status.HTTP_400_BAD_REQUEST)
        product.status = DELETE
        product.save()
        return JsonResponse({'status':True,"msg":"Product Delete Succesfully",})
    except Exception as e:
        return JsonResponse({'status':False, "msg" : str(e)}) 