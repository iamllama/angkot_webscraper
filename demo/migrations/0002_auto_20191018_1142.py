# Generated by Django 2.2.6 on 2019-10-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='routes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
