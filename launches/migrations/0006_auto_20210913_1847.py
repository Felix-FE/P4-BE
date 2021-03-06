# Generated by Django 3.2.7 on 2021-09-13 18:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('launches', '0005_auto_20210913_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='false',
        ),
        migrations.AddField(
            model_name='update',
            name='false',
            field=models.ManyToManyField(blank=True, related_name='verified_false_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='update',
            name='general_announcements',
        ),
        migrations.AddField(
            model_name='update',
            name='general_announcements',
            field=models.ManyToManyField(blank=True, related_name='declared_general_announcement_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='update',
            name='launch_status',
        ),
        migrations.AddField(
            model_name='update',
            name='launch_status',
            field=models.ManyToManyField(blank=True, related_name='declared_status_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='update',
            name='official',
        ),
        migrations.AddField(
            model_name='update',
            name='official',
            field=models.ManyToManyField(blank=True, related_name='verified_official_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='update',
            name='reliable',
        ),
        migrations.AddField(
            model_name='update',
            name='reliable',
            field=models.ManyToManyField(blank=True, related_name='verified_reliable_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='update',
            name='time_change',
        ),
        migrations.AddField(
            model_name='update',
            name='time_change',
            field=models.ManyToManyField(blank=True, related_name='declared_time_change_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='update',
            name='unreliable',
        ),
        migrations.AddField(
            model_name='update',
            name='unreliable',
            field=models.ManyToManyField(blank=True, related_name='verified_unreliable_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
