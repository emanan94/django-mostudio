# Generated by Django 3.1.2 on 2020-10-17 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20201017_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='name',
            new_name='position',
        ),
    ]
