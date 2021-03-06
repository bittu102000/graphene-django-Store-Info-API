# Generated by Django 3.2.8 on 2021-10-08 18:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20211008_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('gst', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='store',
            name='phone_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=225)),
                ('buyer_phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('transaction_time', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.item')),
            ],
        ),
    ]
