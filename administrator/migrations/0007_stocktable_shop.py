# Generated by Django 4.2.17 on 2024-12-24 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_stocktable'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocktable',
            name='SHOP',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.shopprofile'),
        ),
    ]