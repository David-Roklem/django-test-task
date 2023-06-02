# Generated by Django 4.2.1 on 2023-05-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_remember', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=1000)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userpic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('pic', models.CharField(max_length=500)),
            ],
        ),
    ]