# Generated by Django 3.1.3 on 2021-03-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0013_auto_20210311_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='name_of_person',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
