# Generated by Django 2.2.5 on 2019-10-01 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191001_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='no',
            field=models.CharField(default=None, max_length=5),
        ),
    ]