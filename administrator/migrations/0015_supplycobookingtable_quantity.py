# Generated by Django 4.2.17 on 2024-12-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0014_alter_notificationtable_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplycobookingtable',
            name='quantity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]