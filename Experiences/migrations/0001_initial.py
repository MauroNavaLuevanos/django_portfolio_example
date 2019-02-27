# Generated by Django 2.0.5 on 2019-02-12 08:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('position_en', models.CharField(max_length=100, null=True, verbose_name='Position')),
                ('position_es', models.CharField(max_length=100, null=True, verbose_name='Position')),
                ('since', models.DateField(default=datetime.datetime.today, verbose_name='Since')),
                ('until', models.DateField(blank=True, default=datetime.datetime.today, null=True, verbose_name='Until')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_en', models.TextField(null=True, verbose_name='Description')),
                ('description_es', models.TextField(null=True, verbose_name='Description')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Experiences.Company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
            },
        ),
    ]