# Generated by Django 3.0.4 on 2020-04-18 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='units',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
