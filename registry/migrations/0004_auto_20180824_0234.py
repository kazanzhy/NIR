# Generated by Django 2.1 on 2018-08-23 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0003_auto_20180819_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='immunization',
            name='clinic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registry.Clinic'),
        ),
        migrations.AddField(
            model_name='immunization',
            name='contraindications',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='immunization',
            name='general_reaction',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='immunization',
            name='local_reaction',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='token',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='logbook',
            name='date',
            field=models.DateField(),
        ),
    ]
