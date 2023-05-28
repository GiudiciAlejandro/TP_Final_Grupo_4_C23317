# Generated by Django 4.1.7 on 2023-05-14 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=75, verbose_name='Nombre del país')),
            ],
        ),
        migrations.CreateModel(
            name='Doc_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type_name', models.CharField(max_length=50, verbose_name='Tipo de documento')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('worker_surname', models.CharField(max_length=50, verbose_name='Apellido')),
                ('worker_company', models.CharField(max_length=50, verbose_name='Empresa')),
                ('worker_doc_n', models.CharField(max_length=50, verbose_name='N° de documento')),
                ('worker_state', models.BooleanField(verbose_name='Estado')),
                ('worker_comments', models.TextField(max_length=500, verbose_name='Comentarios')),
                ('worker_created', models.DateTimeField()),
                ('worker_deleted', models.DateTimeField(blank=True, null=True)),
                ('worker_doc_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empleados.doc_types')),
                ('worker_nationality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empleados.countries')),
            ],
        ),
    ]