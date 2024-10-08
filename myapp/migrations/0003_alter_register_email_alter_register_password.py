# Generated by Django 5.1 on 2024-09-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=225),
        ),
    ]
