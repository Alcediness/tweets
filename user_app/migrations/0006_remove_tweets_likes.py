# Generated by Django 4.2 on 2023-08-17 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_alter_tweetcomments_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweets',
            name='likes',
        ),
    ]
