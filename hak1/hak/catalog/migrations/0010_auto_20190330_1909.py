# Generated by Django 2.1.5 on 2019-03-30 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20190330_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='action_period',
            field=models.DateField(),
        ),
    ]
