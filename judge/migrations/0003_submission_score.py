# Generated by Django 2.0.7 on 2018-08-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_auto_20180809_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='score',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='content rating'),
        ),
    ]
