# Generated by Django 4.0.4 on 2022-05-03 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_property_propertiesofproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='property',
            field=models.ManyToManyField(through='main.PropertiesOfProduct', to='main.property'),
        ),
    ]
