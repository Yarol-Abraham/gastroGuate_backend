# Generated by Django 4.1.1 on 2022-09-27 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_merge_0003_categoria_0004_tipousuario_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('abreviatura', models.CharField(max_length=20)),
                ('estado', models.IntegerField(default=1, max_length=11)),
                ('id_departamento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.departamento')),
            ],
        ),
    ]
