# Generated by Django 3.1 on 2020-08-22 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20200822_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='city_address_of_bookstore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookstiore', to='location.city'),
        ),
    ]
