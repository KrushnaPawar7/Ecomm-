# Generated by Django 5.0.6 on 2024-06-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BD', 'Bakery&Dairy'), ('GR', 'Grocery'), ('SN', 'Snack'), ('EG', 'Eggs'), ('FV', 'Fruits&vegetable'), ('CH', 'Chocolates')], max_length=2),
        ),
    ]
