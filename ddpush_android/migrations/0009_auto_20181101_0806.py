# Generated by Django 2.1.2 on 2018-11-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddpush_android', '0008_auto_20181101_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='task_id',
            field=models.CharField(max_length=64),
        ),
    ]
