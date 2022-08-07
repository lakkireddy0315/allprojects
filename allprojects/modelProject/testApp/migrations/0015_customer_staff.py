# Generated by Django 3.2.7 on 2022-05-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0014_auto_20220528_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]