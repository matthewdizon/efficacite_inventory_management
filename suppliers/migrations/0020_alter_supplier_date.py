# Generated by Django 4.0.4 on 2022-04-17 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0019_alter_supplier_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 20, 32, 54, 359948), editable=False),
        ),
    ]
