# Generated by Django 3.2.8 on 2022-03-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0006_auto_20220313_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocation',
            name='hour',
            field=models.CharField(default=1, max_length=2, verbose_name='时'),
            preserve_default=False,
        ),
    ]
