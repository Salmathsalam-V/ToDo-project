# Generated by Django 4.1.5 on 2023-09-22 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(blank=True, upload_to='product/'),
        ),
    ]
