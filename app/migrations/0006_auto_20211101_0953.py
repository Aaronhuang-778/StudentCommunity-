# Generated by Django 3.2.8 on 2021-11-01 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211030_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='keyword_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_phone',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
