# Generated by Django 4.2 on 2023-04-19 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='whatsapp',
            field=models.URLField(blank=True, null=True),
        ),
    ]
