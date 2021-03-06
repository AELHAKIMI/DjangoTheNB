# Generated by Django 2.1 on 2018-08-22 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dossierPatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DossierID', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientID', models.CharField(max_length=12)),
                ('patientName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceID', models.CharField(max_length=12)),
                ('service', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='dossierpatient',
            name='patientID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.patient'),
        ),
        migrations.AddField(
            model_name='dossierpatient',
            name='serviceID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.service'),
        ),
    ]
