# Generated by Django 4.0.1 on 2022-01-13 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_remove_propertyspecification_property_features_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='features',
        ),
    ]