# Generated by Django 2.2.6 on 2021-06-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0032_auto_20210604_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='company.png', null=True, upload_to='logo'),
        ),
    ]
