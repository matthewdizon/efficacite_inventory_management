# Generated by Django 4.0.3 on 2022-05-25 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0039_alter_supplier_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 25, 20, 56, 34, 466060), editable=False),
        ),
    ]
