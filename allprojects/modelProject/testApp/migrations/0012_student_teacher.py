# Generated by Django 3.2.7 on 2022-05-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0011_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ID', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
