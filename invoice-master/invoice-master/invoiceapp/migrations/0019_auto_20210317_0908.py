# Generated by Django 3.1.3 on 2021-03-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0018_auto_20210316_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='exchange_rate',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(decimal_places=3, max_digits=13),
        ),
        migrations.AlterField(
            model_name='particular',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=13),
        ),
        migrations.AlterField(
            model_name='particular',
            name='unit_rate',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]
