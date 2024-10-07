# Generated by Django 5.1 on 2024-10-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_name', models.CharField(max_length=255)),
                ('camp_phone', models.CharField(max_length=15)),
                ('requester_name', models.CharField(max_length=255)),
                ('requester_phone', models.CharField(max_length=15)),
                ('resource_type', models.CharField(choices=[('FOOD', 'Food'), ('MEDICAL_SUPPLIES', 'Medical Supplies'), ('VOLUNTEERS', 'Volunteers'), ('EQUIPMENT', 'Equipment'), ('SHELTER', 'Shelter')], max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('request_details', models.TextField()),
                ('delivery_address', models.TextField()),
                ('requested_by_date', models.DateField()),
                ('urgency_level', models.CharField(choices=[('IMMEDIATE', 'Immediate'), ('24_HOURS', 'Next 24 Hours'), ('WEEK', 'Within a Week')], max_length=20)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]