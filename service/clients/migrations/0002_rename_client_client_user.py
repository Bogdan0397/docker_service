# Generated by Django 3.2.16 on 2024-04-03 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client',
            new_name='user',
        ),
    ]
