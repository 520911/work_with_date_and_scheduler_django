# Generated by Django 4.0.2 on 2022-02-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='mobile_code',
            field=models.SmallIntegerField(verbose_name='Mobile operator code'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='mobile_code',
            field=models.SmallIntegerField(verbose_name='Mobile operator code'),
        ),
    ]
