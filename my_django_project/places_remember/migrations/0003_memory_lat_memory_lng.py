# Generated by Django 4.2.1 on 2023-05-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_remember', '0002_memory_userpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='memory',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
