# Generated by Django 3.2.8 on 2022-03-13 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0005_alter_allocation_time_left'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='time_left',
        ),
        migrations.AddField(
            model_name='allocation',
            name='minute',
            field=models.CharField(default=0, max_length=2, verbose_name='分'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allocation',
            name='second',
            field=models.CharField(default=0, max_length=2, verbose_name='秒'),
            preserve_default=False,
        ),
    ]
