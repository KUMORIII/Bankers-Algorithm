# Generated by Django 3.2.8 on 2022-03-13 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0010_allocation_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='idx',
        ),
    ]
