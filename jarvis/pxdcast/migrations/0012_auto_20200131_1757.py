# Generated by Django 3.0.1 on 2020-01-31 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pxdcast', '0011_auto_20200131_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='podcast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pxdcast.Podcast'),
        ),
    ]