# Generated by Django 5.1.5 on 2025-03-20 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_profile_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='y_coordinate',
            new_name='x_percentage',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='x_coordinate',
            new_name='y_percentage',
        ),
    ]
