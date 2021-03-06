# Generated by Django 4.0 on 2022-01-31 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=255)),
                ('friendliness', models.IntegerField(verbose_name=range(1, 5))),
                ('trainability', models.IntegerField(verbose_name=range(1, 5))),
                ('sheddingamount', models.IntegerField(verbose_name=range(1, 5))),
                ('exerciseneeds', models.IntegerField(verbose_name=range(1, 5))),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('favoritefood', models.CharField(max_length=100)),
                ('favoritetoy', models.CharField(max_length=100)),
                ('breed', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapi.breed')),
            ],
        ),
    ]
