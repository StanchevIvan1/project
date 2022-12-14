# Generated by Django 4.1.3 on 2022-12-01 20:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('photo', models.ImageField(default='blank_profile_image.jpeg', upload_to='products')),
                ('description', models.TextField(max_length=300, validators=[django.core.validators.MinLengthValidator(10)])),
                ('price', models.DecimalField(decimal_places=6, max_digits=12, validators=[django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
