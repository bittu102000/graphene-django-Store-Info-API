# Generated by Django 3.2.8 on 2021-10-09 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alter_item_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]