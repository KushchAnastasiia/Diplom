# Generated by Django 2.2 on 2019-04-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('currency', models.CharField(max_length=16)),
                ('guarantee', models.IntegerField(default=0)),
                ('in_case', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=64)),
                ('group', models.CharField(max_length=64)),
                ('subgroup', models.CharField(max_length=64)),
                ('image_path', models.CharField(max_length=256)),
                ('image_name', models.CharField(max_length=256)),
                ('image_type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]
