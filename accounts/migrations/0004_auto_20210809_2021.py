# Generated by Django 3.2.4 on 2021-08-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210809_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='device',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='order',
            name='session_key',
        ),
    ]
