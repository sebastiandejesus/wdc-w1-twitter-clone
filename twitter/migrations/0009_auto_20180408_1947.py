# Generated by Django 2.0 on 2018-04-08 23:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0008_auto_20180408_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 8, 23, 47, 8, 72122, tzinfo=utc)),
        ),
    ]
