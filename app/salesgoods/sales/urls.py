from django.urls import path

from .views import *


urlpatterns = [
    path('', main, name='main_url'),
    path('contacts/', contacts, name='contacts_url'),
    path('products/', products_list, name='products_list_url'),
    path('product/create/', ProductCreate.as_view(), name='product_create_url'),
    path('product/<str:slug>/', ProductDetail.as_view(), name='product_detail_url'),
    path('product/<str:slug>/update/', ProductUpdate.as_view(), name='product_update_url'),
    path('product/<str:slug>/delete/', ProductDelete.as_view(), name='product_delete_url'),
    path('categories/', categories_list, name='categories_list_url'),
    path('category/create/', CategoryCreate.as_view(), name='category_create_url'),
    path('category/<str:slug>/', CategoryDetail.as_view(), name='category_detail_url'),
    path('category/<str:slug>/update/', CategoryUpdate.as_view(), name='category_update_url'),
    path('category/<str:slug>/delete/', CategoryDelete.as_view(), name='category_delete_url')
]