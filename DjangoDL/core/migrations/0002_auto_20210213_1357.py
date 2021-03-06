# Generated by Django 3.1.6 on 2021-02-13 13:57

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='deeplearningmodel',
            name='model',
            field=models.FileField(upload_to='models'),
        ),
        migrations.AlterField(
            model_name='deeplearningmodel',
            name='transformations',
            field=models.JSONField(default=dict, validators=[core.validators.json_validator]),
        ),
        migrations.AlterField(
            model_name='inference',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
