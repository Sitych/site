# Generated by Django 2.1.5 on 2019-03-31 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0033_auto_20190331_0849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'ordering': ['-action_period'], 'verbose_name': 'Меропритятие', 'verbose_name_plural': 'Мероприятия'},
        ),
    ]