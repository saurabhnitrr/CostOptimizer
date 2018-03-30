# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0009_auto_20180330_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculatordata',
            name='total_fare',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calculatordata',
            name='port_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.PortCity'),
        ),
        migrations.AlterField(
            model_name='origintoportair',
            name='port',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.PortCity'),
        ),
        migrations.AlterField(
            model_name='origintoportrail',
            name='port',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.PortCity'),
        ),
        migrations.AlterField(
            model_name='origintoportroad',
            name='port',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.PortCity'),
        ),
        migrations.AlterField(
            model_name='porttodestinationair',
            name='port',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.PortCity'),
        ),
        migrations.AlterField(
            model_name='porttodestinationroad',
            name='port',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.PortCity'),
        ),
        migrations.AlterField(
            model_name='porttodestinationsea',
            name='port',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.PortCity'),
        ),
    ]