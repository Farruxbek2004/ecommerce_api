# Generated by Django 4.2 on 2023-05-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]
