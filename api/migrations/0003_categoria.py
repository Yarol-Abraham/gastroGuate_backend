# Generated by Django 4.1.1 on 2022-09-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_departamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('estado', models.IntegerField(default=1, max_length=1)),
            ],
        ),
    ]