# Generated by Django 3.0.6 on 2020-06-28 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equip', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wherefrom', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=64)),
                ('car_model', models.CharField(max_length=64)),
                ('category', models.IntegerField(choices=[(1, 'osobowe'), (2, 'dostawcze'), (3, 'motocykl')])),
                ('type', models.IntegerField(choices=[(1, 'SUV'), (2, 'sedan'), (3, 'hatchback')])),
                ('year_of_production', models.SmallIntegerField()),
                ('color', models.CharField(max_length=64)),
                ('car_mileage', models.IntegerField()),
                ('description', models.TextField()),
                ('fuel_type', models.IntegerField(choices=[(1, 'benzyna'), (2, 'diesel'), (3, 'LPG'), (4, 'benzyna/lpg'), (4, 'hybryda'), (4, 'elektryczny')])),
                ('doors_number', models.IntegerField(choices=[(1, '3'), (2, '5')])),
                ('seats_number', models.IntegerField(choices=[(1, '2'), (2, '4'), (3, '5'), (4, '6')])),
                ('engine_capacity', models.IntegerField()),
                ('photos', models.ImageField(upload_to='media')),
                ('price', models.IntegerField()),
                ('car_equipment', models.ManyToManyField(to='Auto_Zdam.Equip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auto_Zdam.User')),
            ],
        ),
    ]
