# Generated by Django 5.0.1 on 2024-01-30 04:26

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_doctor_mobile_number_alter_doctor_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
