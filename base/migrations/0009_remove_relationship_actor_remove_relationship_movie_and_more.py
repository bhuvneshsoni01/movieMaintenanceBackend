# Generated by Django 4.1.6 on 2023-02-14 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_relationship_actor_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='movie',
        ),
        migrations.AddField(
            model_name='relationship',
            name='actor_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='relationship',
            name='movie_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
