# Generated by Django 3.1.3 on 2021-06-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0045_currency_currency_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='cgst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='sgst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
