# Generated by Django 2.2.6 on 2021-06-04 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0033_auto_20210604_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='project_type',
            field=models.CharField(blank=True, choices=[('fixed bid', 'Fixed Price'), ('hourly', 'Hourly')], max_length=50, null=True),
        ),
    ]
