# Generated by Django 2.2.4 on 2022-10-11 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20221011_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='location',
        ),
    ]