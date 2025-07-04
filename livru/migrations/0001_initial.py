# Generated by Django 5.2.1 on 2025-06-01 03:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id_kategoria', models.AutoField(primary_key=True, serialize=False)),
                ('naran_kategoria', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Livru',
            fields=[
                ('id_livru', models.AutoField(primary_key=True, serialize=False)),
                ('titulu_livru', models.CharField(max_length=60)),
                ('isbn', models.CharField(max_length=20)),
                ('data_publica', models.DateField()),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autor.autor')),
                ('id_kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livru.kategoria')),
                ('id_publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='LivruKopia',
            fields=[
                ('id_kopia', models.AutoField(primary_key=True, serialize=False)),
                ('barcode', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('available', 'Available'), ('borrowed', 'Borrowed')], default='available', max_length=50)),
                ('id_livru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kopia', to='livru.livru')),
            ],
        ),
    ]
