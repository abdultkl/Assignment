# Generated by Django 3.2.9 on 2021-11-30 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency_code', models.CharField(max_length=20)),
                ('from_currency_name', models.CharField(max_length=20)),
                ('to_currency_code', models.CharField(max_length=20)),
                ('to_currency_name', models.CharField(max_length=20)),
                ('exchange_rate', models.DecimalField(decimal_places=8, max_digits=18)),
                ('last_refreshed', models.DateTimeField()),
                ('time_zone', models.CharField(max_length=10)),
                ('bid_price', models.DecimalField(decimal_places=8, max_digits=18)),
                ('ask_price', models.DecimalField(decimal_places=8, max_digits=18)),
            ],
            options={
                'db_table': 'prices',
            },
        ),
    ]
