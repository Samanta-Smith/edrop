# Generated by Django 2.2.9 on 2020-01-28 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20200127_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='items',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 5, 38, 14, 751004)),
        ),
    ]
