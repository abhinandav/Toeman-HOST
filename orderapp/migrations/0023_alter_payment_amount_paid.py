# Generated by Django 4.2.6 on 2023-12-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0022_orderproduct_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount_paid',
            field=models.FloatField(default=0),
        ),
    ]
