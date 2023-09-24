# Generated by Django 4.2.5 on 2023-09-23 13:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coalstock',
            name='siding',
        ),
        migrations.AddField(
            model_name='coalstock',
            name='capacity',
            field=models.IntegerField(default=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coalstock',
            name='location',
            field=models.CharField(default=(23.166544, 79.946041), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coalstock',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Siding',
        ),
    ]
