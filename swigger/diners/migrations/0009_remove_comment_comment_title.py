# Generated by Django 2.0.7 on 2018-09-10 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diners', '0008_visited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_title',
        ),
    ]
