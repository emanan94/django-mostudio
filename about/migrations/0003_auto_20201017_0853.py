# Generated by Django 3.1.2 on 2020-10-17 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20201017_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ceo',
            old_name='text',
            new_name='quotation',
        ),
    ]
