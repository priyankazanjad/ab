# Generated by Django 3.1.7 on 2021-03-03 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0006_bankaccounttype_currency_resourcetype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='particular',
            name='item_name',
        ),
        migrations.AddField(
            model_name='particular',
            name='resource_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='invoiceapp.resourcetype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companybankdetail',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoiceapp.bankaccounttype'),
        ),
    ]
