# Generated by Django 4.1.7 on 2023-05-30 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epp', '0012_rename_epp_inps_epp_epp_inspections_epp_inps_epp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epp_inspections',
            name='epp_insp_status',
            field=models.TextField(verbose_name='Resultado'),
        ),
    ]
