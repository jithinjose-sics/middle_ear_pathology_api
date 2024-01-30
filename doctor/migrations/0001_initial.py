# Generated by Django 5.0.1 on 2024-01-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('mobile_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('hospital_name', models.CharField(max_length=100)),
                ('doctor_id_number', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]