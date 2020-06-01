from django.shortcuts import render, redirect
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Product, Category
from .utils import *
from .forms import CategoryForm, ProductForm

from django.contrib.auth.mixins import LoginRequiredMixin


def products_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        products = Product.objects.filter(title__icontains=search_query)
    else:
        products = Product.objects.all()
    return render(request, 'sales/index.html', context={'products': products})



class ProductCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = ProductForm
    template = 'sales/product_create.html'
    raise_exception = True


class ProductUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Product
    model_form = ProductForm
    template = 'sales/product_update.html'
    raise_exception = True


class ProductDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Product
    template = 'sales/product_delete.html'
    redirect_url = 'products_list_url'
    raise_exception = True


class ProductDetail(ObjectDetailMixin, View):
    model = Product
    template = 'sales/product_detail.html'


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'sales/categories_list.html', context={'categories': categories})


class CategoryCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = CategoryForm
    template = 'sales/category_create.html'
    raise_exception = True


class CategoryUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Category
    model_form = CategoryForm
    template = 'sales/category_update.html'
    raise_exception = True


class CategoryDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Category
    template = 'sales/category_delete.html'
    redirect_url = 'categories_list_url'
    raise_exception = True


class CategoryDetail(ObjectDetailMixin, View):
    model = Category
    template = 'sales/category_detail.html'


def main(request):
    return render(request, 'sales/main.html', context={'main': main})


def contacts(request):
    return render(request, 'sales/contacts.html', context={'contacts': contacts})


