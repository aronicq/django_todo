# Generated by Django 3.1.3 on 2020-12-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_todo_app', '0008_auto_20201130_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='title',
            field=models.CharField(default='dafault title', max_length=20),
            preserve_default=False,
        ),
    ]