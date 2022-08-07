# Generated by Django 3.2.7 on 2021-11-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0003_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=30)),
                ('pages', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
