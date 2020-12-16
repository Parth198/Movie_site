# Generated by Django 3.1.4 on 2020-12-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_Data',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('poster_path', models.CharField(max_length=100)),
                ('overview', models.CharField(max_length=1000)),
                ('popularity', models.FloatField()),
            ],
        ),
    ]
