# Generated by Django 4.2.8 on 2024-01-06 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='opening',
            field=models.BooleanField(default=False),
        ),
    ]
