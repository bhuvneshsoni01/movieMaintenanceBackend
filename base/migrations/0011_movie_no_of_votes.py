# Generated by Django 4.1.6 on 2023-02-14 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_relationship_actor_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='no_of_votes',
            field=models.IntegerField(default=0),
        ),
    ]