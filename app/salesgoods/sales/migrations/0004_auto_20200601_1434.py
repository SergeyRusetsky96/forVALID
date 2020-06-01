# Generated by Django 3.0.6 on 2020-06-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_category_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]
