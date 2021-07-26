# Generated by Django 3.1.5 on 2021-07-26 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postulante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entrevista', models.CharField(max_length=6)),
                ('Nota', models.CharField(max_length=2)),
                ('Detalles', models.TextField()),
                ('Postulante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postulante.postulante')),
            ],
        ),
    ]