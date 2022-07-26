# Generated by Django 4.0.6 on 2022-07-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientAppointment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('appointment_start_time', models.TimeField(verbose_name='Appointment start time')),
                ('appointment_end_time', models.TimeField(verbose_name='Appointment end time')),
                ('description', models.CharField(max_length=1024, verbose_name='Enter description')),
                ('pet_type', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('BITCOIN', 'BITCOIN')], max_length=15, verbose_name='Select Pet Type')),
                ('unpaid_amount', models.CharField(max_length=50, verbose_name='Enter unpaid amount')),
                ('total_amount', models.CharField(max_length=50, verbose_name='Enter total amount')),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
