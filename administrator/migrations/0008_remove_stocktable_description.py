# Generated by Django 4.2.17 on 2024-12-24 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0007_stocktable_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocktable',
            name='description',
        ),
    ]