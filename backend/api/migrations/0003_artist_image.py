# Generated by Django 2.0.1 on 2018-01-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_artist_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.CharField(default='default.png', max_length=150),
            preserve_default=False,
        ),
    ]