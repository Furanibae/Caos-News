# Generated by Django 5.0.4 on 2024-06-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_nombreprod_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='mensual.png', upload_to='cart/products/'),
        ),
    ]
