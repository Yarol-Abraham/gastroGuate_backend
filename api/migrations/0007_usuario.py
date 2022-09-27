# Generated by Django 4.1.1 on 2022-09-27 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_municipio'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('usuario', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('identificacion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.IntegerField(default=1, max_length=11)),
                ('id_municipio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.municipio')),
                ('id_tipousuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.tipousuario')),
            ],
        ),
    ]
