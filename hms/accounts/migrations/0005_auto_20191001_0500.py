# Generated by Django 2.2.5 on 2019-10-01 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191001_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='no',
            field=models.CharField(blank=True, default=None, max_length=5, null=True),
        ),
    ]
