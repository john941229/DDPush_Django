# Generated by Django 2.1.2 on 2018-11-01 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddpush_wx', '0002_auto_20181101_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='wx_bindDate',
            field=models.CharField(max_length=50),
        ),
    ]