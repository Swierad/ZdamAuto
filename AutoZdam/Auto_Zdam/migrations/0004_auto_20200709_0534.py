# Generated by Django 3.0.6 on 2020-07-09 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auto_Zdam', '0003_auto_20200708_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='photos_2',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='offer',
            name='photos_3',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='offer',
            name='photos_4',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='offer',
            name='photos_5',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
