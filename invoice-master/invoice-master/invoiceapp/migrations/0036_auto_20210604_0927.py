# Generated by Django 3.1.3 on 2021-06-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0035_merge_20210604_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='project_type',
            field=models.CharField(blank=True, choices=[('fixed price', 'Fixed Price'), ('hourly', 'Hourly')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='project_type',
            field=models.CharField(choices=[('fixed price', 'Fixed Price'), ('hourly', 'Hourly')], default='hourly', max_length=50),
        ),
    ]
