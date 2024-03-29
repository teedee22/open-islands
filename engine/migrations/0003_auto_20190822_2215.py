# Generated by Django 2.2.4 on 2019-08-22 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_auto_20190822_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='Gold',
            new_name='gold',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='Lumber',
            new_name='lumber',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='Score',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='Stone',
            new_name='stone',
        ),
        migrations.AddField(
            model_name='player',
            name='buildings',
            field=models.ManyToManyField(blank=True, to='engine.Building'),
        ),
    ]
