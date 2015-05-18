# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_movie_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cover',
            field=models.ImageField(upload_to='', default=''),
            preserve_default=False,
        ),
    ]
