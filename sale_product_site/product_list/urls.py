from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('/shop/<shop_name>', view_products, name='shop'),
    path('/shop/<shop_name>/<category>', view_products_category),
]