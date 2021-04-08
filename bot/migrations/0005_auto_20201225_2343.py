# Generated by Django 3.1.4 on 2020-12-25 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_vlivesubscribedchannel_dev_channel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vlivesubscribedchannel',
            options={'ordering': ['group__name', 'channel_id']},
        ),
        migrations.AlterField(
            model_name='member',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='bot.group'),
        ),
        migrations.AlterField(
            model_name='twittermediasource',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twitter_media_sources', to='bot.member'),
        ),
        migrations.AlterField(
            model_name='twittermediasubscribedchannel',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twitter_media_subscribed_channels', to='bot.group'),
        ),
        migrations.AlterField(
            model_name='vlivesubscribedchannel',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vlive_subscribed_channels', to='bot.group'),
        ),
    ]
