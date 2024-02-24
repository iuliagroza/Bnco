# Generated by Django 3.1.3 on 2023-03-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('iban', models.CharField(max_length=34)),
                ('bicswift', models.CharField(max_length=11)),
                ('balance', models.FloatField()),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
    ]