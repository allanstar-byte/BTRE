# Generated by Django 4.1.5 on 2023-02-07 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='desctiption',
            new_name='description',
        ),
    ]