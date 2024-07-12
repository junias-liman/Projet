# Generated by Django 5.0.6 on 2024-05-23 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPress', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Mail', models.EmailField(max_length=254)),
                ('Nummber', models.CharField(max_length=50)),
                ('Adresse', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='depot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_vêtements', models.CharField(max_length=50)),
                ('montant', models.IntegerField()),
                ('date_depot', models.DateField()),
                ('date_retrait', models.DateField(blank=True)),
                ('marque', models.CharField(max_length=50)),
                ('Regler', models.BooleanField(default=False)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPress.client')),
            ],
        ),
    ]