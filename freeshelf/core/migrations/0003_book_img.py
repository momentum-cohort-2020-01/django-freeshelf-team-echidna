# Generated by Django 3.0.3 on 2020-03-01 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200228_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
