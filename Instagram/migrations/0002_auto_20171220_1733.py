# Generated by Django 2.0 on 2017-12-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='photo',
            field=models.ImageField(upload_to='Instagram/static/Instagram/images'),
        ),
    ]
