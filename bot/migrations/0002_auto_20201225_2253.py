# Generated by Django 3.1.4 on 2020-12-25 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='vlive_channel_code',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='vlive_channel_seq',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='vlive_last_seq',
            field=models.BigIntegerField(null=True),
        ),
    ]
