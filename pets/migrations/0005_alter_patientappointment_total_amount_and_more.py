# Generated by Django 4.0.6 on 2022-07-26 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_remove_patientappointment_paynment_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientappointment',
            name='total_amount',
            field=models.IntegerField(verbose_name='Enter total amount'),
        ),
        migrations.AlterField(
            model_name='patientappointment',
            name='unpaid_amount',
            field=models.IntegerField(verbose_name='Enter unpaid amount'),
        ),
    ]