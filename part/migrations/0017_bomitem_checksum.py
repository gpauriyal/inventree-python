# Generated by Django 2.2.4 on 2019-09-05 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0016_auto_20190820_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='bomitem',
            name='checksum',
            field=models.CharField(blank=True, help_text='BOM line checksum', max_length=128),
        ),
    ]
