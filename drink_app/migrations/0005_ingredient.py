# Generated by Django 3.0.8 on 2020-07-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink_app', '0004_extra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
