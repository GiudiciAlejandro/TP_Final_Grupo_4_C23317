# Generated by Django 4.1.7 on 2023-05-30 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epp', '0015_alter_epp_inspections_epp_inps_epp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epp_inspections',
            name='epp_inps_epp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epp_related', to='epp.epp'),
        ),
    ]
