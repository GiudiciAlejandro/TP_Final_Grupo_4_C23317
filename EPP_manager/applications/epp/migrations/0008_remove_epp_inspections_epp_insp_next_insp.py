# Generated by Django 4.1.7 on 2023-05-29 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epp', '0007_alter_epp_epp_assigned_alter_epp_epp_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='epp_inspections',
            name='epp_insp_next_insp',
        ),
    ]
