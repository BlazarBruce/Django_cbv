# Generated by Django 2.2.6 on 2019-10-12 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_id',
            field=models.IntegerField(verbose_name='id'),
        ),
    ]
