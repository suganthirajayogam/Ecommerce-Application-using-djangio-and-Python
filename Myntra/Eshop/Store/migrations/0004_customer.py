# Generated by Django 4.2.16 on 2025-01-09 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=25)),
                ('Mobno', models.CharField(max_length=15)),
                ('Emailid', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=500)),
            ],
        ),
    ]
