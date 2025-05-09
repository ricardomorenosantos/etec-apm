# Generated by Django 5.2 on 2025-04-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('data_reuniao', models.DateField()),
                ('arquivo', models.FileField(upload_to='atas/')),
            ],
        ),
        migrations.CreateModel(
            name='TermoPosse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membro_nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=50)),
                ('data_posse', models.DateField()),
                ('arquivo', models.FileField(upload_to='termos/')),
            ],
        ),
    ]
