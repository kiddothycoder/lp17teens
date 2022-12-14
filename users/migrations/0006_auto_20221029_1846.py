# Generated by Django 3.1.4 on 2022-10-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_sociallink'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Zone', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='Zone',
            field=models.ManyToManyField(related_name='posts', to='users.ChurchCategory'),
        ),
    ]
