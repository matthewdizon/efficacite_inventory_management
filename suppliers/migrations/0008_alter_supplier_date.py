# Generated by Django 4.0.3 on 2022-03-26 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0007_alter_supplier_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 26, 18, 33, 3, 710584), editable=False),
        ),
    ]
