# Generated by Django 4.0.5 on 2022-06-22 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_id', models.CharField(max_length=200)),
                ('album_name', models.CharField(max_length=500)),
                ('album_url', models.URLField()),
                ('album_label', models.CharField(max_length=1000)),
                ('album_type', models.CharField(max_length=300)),
                ('artist_name', models.CharField(max_length=200)),
                ('total_tracks', models.IntegerField()),
                ('release_date', models.DateField()),
                ('is_new', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.CharField(max_length=200)),
                ('track_name', models.CharField(max_length=1000)),
                ('duration_ms', models.IntegerField()),
                ('artist', models.CharField(max_length=200)),
                ('track_url', models.URLField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotapp.album')),
            ],
        ),
    ]
