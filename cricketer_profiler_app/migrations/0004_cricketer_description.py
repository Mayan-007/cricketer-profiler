# Generated by Django 3.2.19 on 2023-06-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketer_profiler_app', '0003_delete_coachteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='cricketer',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]