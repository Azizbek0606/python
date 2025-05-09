# Generated by Django 4.2.20 on 2025-05-05 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pages', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DigitalMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file_format', models.CharField(max_length=50)),
                ('file_size', models.FloatField(help_text='Size in MB')),
                ('url', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pages', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
