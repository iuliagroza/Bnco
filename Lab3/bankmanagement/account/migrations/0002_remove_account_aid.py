# Generated by Django 3.1.3 on 2023-03-04 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='aid',
        ),
    ]
