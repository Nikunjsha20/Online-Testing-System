# Generated by Django 5.0.6 on 2024-12-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='points',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='test_attempted',
            field=models.IntegerField(default=0),
        ),
    ]
