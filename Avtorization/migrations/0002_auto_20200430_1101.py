# Generated by Django 3.0.5 on 2020-04-30 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Avtorization', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]
