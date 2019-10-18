# Generated by Django 2.2.6 on 2019-10-10 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=100, verbose_name='id')),
                ('user_name', models.CharField(max_length=100, verbose_name='name')),
                ('user_token', models.CharField(max_length=100, verbose_name='token')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
