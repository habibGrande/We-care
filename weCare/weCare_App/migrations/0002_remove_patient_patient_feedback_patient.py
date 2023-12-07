# Generated by Django 4.2.7 on 2023-12-07 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weCare_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patient',
        ),
        migrations.AddField(
            model_name='feedback',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='weCare_App.patient'),
        ),
    ]