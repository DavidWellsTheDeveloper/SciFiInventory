# Generated by Django 3.0.4 on 2020-03-28 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField(null=True)),
                ('sku', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Component')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Part')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('intake', models.BooleanField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Part')),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.System'),
        ),
    ]