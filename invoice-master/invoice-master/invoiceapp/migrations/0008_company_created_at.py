# Generated by Django 2.2.6 on 2021-03-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0007_auto_20210303_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
