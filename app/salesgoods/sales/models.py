from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug


class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, related_name='products')

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('product_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('product_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    body = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('category_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('category_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)
