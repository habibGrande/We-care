# Generated by Django 4.2.7 on 2023-12-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weCare_App', '0002_remove_patient_patient_feedback_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='appointments',
            field=models.ManyToManyField(null=True, through='weCare_App.Appointment', to='weCare_App.patient'),
        ),
    ]
