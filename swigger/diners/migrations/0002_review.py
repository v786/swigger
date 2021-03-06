# Generated by Django 2.0.7 on 2018-07-10 16:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=200)),
                ('review_text', models.TextField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('diner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diners.Diner')),
            ],
        ),
    ]
