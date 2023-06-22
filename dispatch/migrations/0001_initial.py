# Generated by Django 4.2.2 on 2023-06-22 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='LicensePlate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_type', models.CharField(choices=[('Municipal', (('MVN', 'Municipal Vehicle'), ('MXN', 'Municipal Motorcycle'))), ('Passenger', (('PAN', 'Passenger Normal'),)), ('XXX', 'Unknown')], default='MVN', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('variety', models.CharField(max_length=32)),
                ('radio_id', models.CharField(max_length=4)),
                ('license_plate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dispatch.licenseplate')),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('radio_id', models.CharField(max_length=32)),
                ('active_call', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dispatch.call')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dispatch.vehicle')),
            ],
        ),
    ]
