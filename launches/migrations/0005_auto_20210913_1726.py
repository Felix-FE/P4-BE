# Generated by Django 3.2.7 on 2021-09-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launches', '0004_auto_20210913_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='false',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='general_announcements',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='launch_status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='official',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='reliable',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='time_change',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='unreliable',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
