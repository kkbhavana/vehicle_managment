# Generated by Django 4.2.4 on 2023-08-14 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=15)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_description', models.TextField()),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='vehicle.types')),
            ],
        ),
    ]