# Generated by Django 4.2.7 on 2024-10-07 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AidTogether', '0007_alter_organisationprofile_org_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationprofile',
            name='org_image',
            field=models.ImageField(upload_to='profileimages'),
        ),
        migrations.AlterField(
            model_name='reliefcampprofile',
            name='camp_image',
            field=models.ImageField(upload_to='profileimages'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='vol_image',
            field=models.ImageField(upload_to='profileimages'),
        ),
    ]
