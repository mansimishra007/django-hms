# Generated by Django 2.2.5 on 2019-09-27 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190927_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Room'),
        ),
    ]