# Generated by Django 3.1.4 on 2021-01-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_attribute_training_trainingvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingvalue',
            name='value',
            field=models.FloatField(null=True),
        ),
    ]
