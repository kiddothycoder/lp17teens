# Generated by Django 3.1.4 on 2022-11-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_vidstream_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vidstream',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
