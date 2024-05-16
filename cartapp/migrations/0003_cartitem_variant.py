# Generated by Django 4.2.6 on 2023-12-01 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_remove_products_quantity_remove_products_sizes_and_more'),
        ('cartapp', '0002_cartitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.productattribute'),
            preserve_default=False,
        ),
    ]
