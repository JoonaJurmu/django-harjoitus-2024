# Generated by Django 5.0.1 on 2024-01-29 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kysymys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teksti', models.CharField(max_length=200)),
                ('julkaisupvm', models.DateTimeField(verbose_name='julkaistu')),
            ],
        ),
        migrations.CreateModel(
            name='Vaihtoehto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teksti', models.CharField(max_length=200)),
                ('ääniä', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kysely.kysymys')),
            ],
        ),
    ]
