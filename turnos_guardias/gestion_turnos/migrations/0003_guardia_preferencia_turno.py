# Generated by Django 5.1 on 2024-12-17 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_turnos', '0002_disponibilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardia',
            name='preferencia_turno',
            field=models.IntegerField(choices=[(1, 'Mañana'), (2, 'Tarde'), (3, 'Noche')], default=1),
        ),
    ]
