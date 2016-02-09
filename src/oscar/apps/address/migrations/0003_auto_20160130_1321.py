# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20160130_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='country',
            field=models.ForeignKey(verbose_name='Country', blank=True, to='address.Country'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='phone_number',
            field=models.CharField(help_text='In case we need to call you about your order', max_length=30, verbose_name='Phone number', blank=True),
        ),
    ]
