# Generated by Django 4.0.3 on 2022-05-22 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0029_alter_supplier_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 22, 17, 41, 30, 172573), editable=False),
        ),
    ]
