# Generated by Django 4.2 on 2023-08-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0008_remove_tweets_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='Beğeni'),
        ),
    ]