# Generated by Django 4.0.3 on 2022-05-22 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0006_alter_ingredient_id'),
        ('orders', '0010_remove_order_ingredient_order_order_product_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_order',
        ),
        migrations.AddField(
            model_name='order',
            name='ingredient_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ingredients.ingredient'),
        ),
    ]
