# Generated by Django 4.0.4 on 2023-02-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0020_alter_schedulesubscriber_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schedulesubscriber',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='schedulesubscriber',
            name='guild_id',
            field=models.BigIntegerField(db_index=True, unique=True),
        ),
    ]