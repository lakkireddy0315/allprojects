# Generated by Django 3.2.7 on 2022-08-27 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0003_album_author_book_car_song_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projectApp.album'),
        ),
    ]
