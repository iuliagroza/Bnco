# Generated by Django 3.1.3 on 2023-03-12 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bicswift', models.CharField(max_length=18)),
                ('address', models.TextField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.bank')),
            ],
        ),
    ]
