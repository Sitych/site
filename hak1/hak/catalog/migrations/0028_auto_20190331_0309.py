# Generated by Django 2.1.5 on 2019-03-31 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_auto_20190331_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Face1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Физ. лицо', 'Физическое лицо')], max_length=20, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='partnerindividual',
            options={'verbose_name': 'Партнер физ. лицо', 'verbose_name_plural': 'Партнеры физ. лица'},
        ),
        migrations.AlterField(
            model_name='face',
            name='name',
            field=models.CharField(choices=[('Юр. лицо', 'Юридическое лицо')], max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='face',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Face1'),
        ),
        migrations.AlterField(
            model_name='partnerindividual',
            name='contact_feedback',
            field=models.TextField(help_text='Чем закончилась встреча', max_length=1000, verbose_name='Обратная связь'),
        ),
        migrations.AlterField(
            model_name='partnerindividual',
            name='contact_info',
            field=models.CharField(help_text='История взаимоотношений с партнером (когда и по какому каналу (e-mail, телефон, личная встреча и т.п.) мы ранее общались', max_length=50, verbose_name='Последняя связь'),
        ),
        migrations.AlterField(
            model_name='partnerindividual',
            name='goal',
            field=models.ManyToManyField(to='catalog.Problem', verbose_name='Задачи'),
        ),
    ]
