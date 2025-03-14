# Generated by Django 5.1.7 on 2025-03-14 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_location_game_name'),
        ('minigames', '0002_game_remove_gamescore_location_gamescore_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='game_name',
        ),
        migrations.AddField(
            model_name='location',
            name='game',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='minigames.game'),
        ),
    ]
