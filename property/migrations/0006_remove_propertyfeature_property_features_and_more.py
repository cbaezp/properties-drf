# Generated by Django 4.0.1 on 2022-01-13 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_remove_property_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyfeature',
            name='property_features',
        ),
        migrations.AlterField(
            model_name='propertyspecification',
            name='specification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_specification', to='property.propertyfeature'),
        ),
    ]
