# Generated by Django 3.1.2 on 2020-10-17 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='photos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricing_photos', to='pricing.photos'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='processing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricing_processing', to='pricing.processing'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricing_resolution', to='pricing.resolution'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricing_term', to='pricing.term'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='type_of_camera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricing_typeofcameray', to='pricing.typeofcamera'),
        ),
    ]