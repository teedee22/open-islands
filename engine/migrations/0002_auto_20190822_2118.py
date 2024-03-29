# Generated by Django 2.2.4 on 2019-08-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gold', models.IntegerField(default=200)),
                ('Lumber', models.IntegerField(default=200)),
                ('Stone', models.IntegerField(default=200)),
                ('Score', models.IntegerField(default=1)),
                ('last_action', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]
