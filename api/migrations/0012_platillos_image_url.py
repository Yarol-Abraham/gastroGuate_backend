# Generated by Django 4.1.1 on 2022-10-19 03:54

import api.models.modelPlatillos
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_usuario_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='platillos',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.modelPlatillos.upload_to),
        ),
    ]
