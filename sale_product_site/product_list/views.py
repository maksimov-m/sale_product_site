from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
# Create your views here.

def index(request):
    r = requests.get('http://45.143.94.139/Discount/Shops')
    content = r.json()
    print(content[0])
    return render(request, 'product_list/index.html', {'shops' : content})

def view_products(request, shop_name):
    category = request.GET.get("category", " ")
    r = requests.get(f'http://45.143.94.139/Discount/Products?ShopName={shop_name}&Category={category}&Page=0')
    content = r.json()
    return render(request, 'product_list/view_products.html', {'content' : content['products'], 'shop_name': shop_name})

def view_products_category(request, shop_name, category):
    r = requests.get(f'http://45.143.94.139/Discount/Products?ShopName={shop_name}&Category={category}&Page=0')
    content = r.json()
    return render(request, 'product_list/view_products.html', {'content': content['products'], 'shop_name': shop_name})
