# Generated by Django 4.1.2 on 2023-05-12 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=30)),
                ('value', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='applicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rollno', models.IntegerField()),
                ('phoneno', models.IntegerField()),
                ('fatherName', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('semester', models.CharField(max_length=255)),
                ('hostelNumber', models.CharField(max_length=255)),
                ('roomNumber', models.IntegerField()),
                ('fromDate', models.DateField()),
                ('time', models.TimeField()),
                ('toDate', models.DateField()),
                ('reason', models.CharField(max_length=500)),
                ('parentContact', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]
