# Generated by Django 5.1.7 on 2025-03-18 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='Category'),
            preserve_default=False,
        ),
    ]
