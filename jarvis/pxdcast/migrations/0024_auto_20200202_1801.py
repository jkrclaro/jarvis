# Generated by Django 3.0.1 on 2020-02-02 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pxdcast', '0023_auto_20200202_1756'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='episode',
            unique_together={('name', 'uploaded_at', 'duration', 'url', 'podcast')},
        ),
    ]
