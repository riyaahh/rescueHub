# Generated by Django 5.1 on 2024-10-30 13:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('org_image', models.ImageField(upload_to='profileimages')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReliefCampProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('camp_image', models.ImageField(upload_to='profileimages')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=20)),
                ('vol_image', models.ImageField(upload_to='profileimages')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
