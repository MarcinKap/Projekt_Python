# Generated by Django 3.0.7 on 2020-06-16 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project_Python', '0003_auto_20200615_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentPhase',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project_Python.Tournament')),
            ],
        ),
    ]
