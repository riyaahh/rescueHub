# Generated by Django 4.2.7 on 2024-09-09 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AidTogether', '0003_remove_volunteerprofile_role_organisationprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReliefCampProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
