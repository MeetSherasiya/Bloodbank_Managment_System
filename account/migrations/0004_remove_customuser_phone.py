# Generated by Django 4.2.6 on 2023-10-07 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customuser_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
    ]
