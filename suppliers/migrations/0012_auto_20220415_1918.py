# Generated by Django 2.0 on 2022-04-15 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0011_auto_20220415_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 15, 19, 18, 40, 824241), editable=False),
        ),
    ]