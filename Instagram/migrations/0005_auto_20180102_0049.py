# Generated by Django 2.0 on 2018-01-02 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0004_auto_20171220_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='photo',
            field=models.ImageField(upload_to='Instagram/static/Instagram/images'),
        ),
    ]
