# Generated by Django 3.0.8 on 2020-07-27 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink_app', '0005_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='subsitute1',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='drink',
            name='subsitute2',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='drink',
            name='subsitute3',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='drink',
            name='subsitute4',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='drink',
            name='subsitute5',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='drink',
            name='subsitute6',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='drink',
            name='subsitute7',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='drink',
            name='subsitute8',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
