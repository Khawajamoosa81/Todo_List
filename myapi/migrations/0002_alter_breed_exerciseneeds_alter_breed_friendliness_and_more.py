# Generated by Django 4.0 on 2022-01-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='exerciseneeds',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='breed',
            name='friendliness',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='breed',
            name='sheddingamount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='breed',
            name='trainability',
            field=models.IntegerField(),
        ),
    ]
