# Generated by Django 3.1.4 on 2021-01-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_auto_20210102_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='vlive_channel_seq',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='vlive_last_seq',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
