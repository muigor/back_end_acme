# Generated by Django 3.0 on 2023-02-24 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230223_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regle',
            name='exercices',
        ),
        migrations.RemoveField(
            model_name='ue',
            name='enseignants',
        ),
    ]
