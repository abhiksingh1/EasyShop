# Generated by Django 2.2.6 on 2019-10-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20191015_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=1000),
        ),
    ]
