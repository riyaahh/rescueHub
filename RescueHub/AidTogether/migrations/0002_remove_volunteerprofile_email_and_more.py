# Generated by Django 5.1 on 2024-09-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AidTogether', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='volunteerprofile',
            name='password',
        ),
        migrations.AddField(
            model_name='volunteerprofile',
            name='role',
            field=models.CharField(choices=[('volunteer', 'Volunteer'), ('organisation', 'Organisation'), ('relief_camp', 'Relief Camp')], default='volunteer', max_length=20),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
