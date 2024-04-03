# Generated by Django 3.2.16 on 2024-04-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_type',
            field=models.CharField(choices=[('full', 'Full'), ('student', 'Student'), ('discount', 'Discount')], max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
