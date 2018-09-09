# Generated by Django 2.0.7 on 2018-09-07 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diners', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_title', models.CharField(max_length=200)),
                ('comment_text', models.TextField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='diner',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='author',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diners.Review'),
        ),
    ]
