# Generated by Django 4.2 on 2023-04-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='media/blogs')),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
    ]
