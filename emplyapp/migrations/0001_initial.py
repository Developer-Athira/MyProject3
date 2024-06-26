# Generated by Django 4.2.7 on 2023-12-21 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('dob', models.DateField(default=datetime.date(2023, 1, 1))),
                ('dateOfJ', models.DateField(default=datetime.date(2023, 1, 1))),
                ('department', models.IntegerField()),
                ('is_Admin', models.BooleanField(default=False)),
            ],
        ),
    ]
