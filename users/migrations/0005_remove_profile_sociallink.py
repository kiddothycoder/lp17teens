# Generated by Django 3.1.4 on 2022-10-29 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220924_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='SocialLink',
        ),
    ]
