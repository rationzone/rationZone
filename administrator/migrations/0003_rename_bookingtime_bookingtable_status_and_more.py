# Generated by Django 4.2.17 on 2024-12-23 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_usertable_name_alter_shopprofile_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingtable',
            old_name='bookingtime',
            new_name='STATUS',
        ),
        migrations.RemoveField(
            model_name='bookingtable',
            name='LOGINID',
        ),
        migrations.RemoveField(
            model_name='bookingtable',
            name='customerid',
        ),
        migrations.RemoveField(
            model_name='bookingtable',
            name='productid',
        ),
        migrations.RemoveField(
            model_name='complainttable',
            name='customerid',
        ),
        migrations.RemoveField(
            model_name='feedbacktable',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='feedbacktable',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='producttable',
            name='LOGINID',
        ),
        migrations.RemoveField(
            model_name='shopprofile',
            name='location',
        ),
        migrations.AddField(
            model_name='bookingtable',
            name='PRODUCT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.producttable'),
        ),
        migrations.AddField(
            model_name='bookingtable',
            name='USERID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.usertable'),
        ),
        migrations.AddField(
            model_name='bookingtable',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complainttable',
            name='USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.usertable'),
        ),
        migrations.AddField(
            model_name='complainttable',
            name='reply',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feedbacktable',
            name='USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.usertable'),
        ),
        migrations.AddField(
            model_name='feedbacktable',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='producttable',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='producttable',
            name='image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producttable',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shopprofile',
            name='LOGINID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.logintable'),
        ),
        migrations.AddField(
            model_name='shopprofile',
            name='closingtime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='complainttable',
            name='datetime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbacktable',
            name='feedback',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='notificationtable',
            name='datetime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producttable',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shopprofile',
            name='openningtime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]