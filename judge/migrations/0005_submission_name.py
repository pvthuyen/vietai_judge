# Generated by Django 2.0.7 on 2018-08-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0004_auto_20180809_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
