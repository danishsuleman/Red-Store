# Generated by Django 4.0.5 on 2022-07-19 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_tag_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured_image',
            field=models.FileField(upload_to='Products'),
        ),
    ]