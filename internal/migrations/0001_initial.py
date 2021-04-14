# Generated by Django 3.1.7 on 2021-03-23 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('1', 'Corporate HeadOfiice'), ('2', 'Operation Department'), ('3', 'Work station'), ('4', 'Marketing Division')], default='1', max_length=100, verbose_name='Location')),
                ('description', models.TextField(verbose_name='Incident department')),
                ('time', models.DateTimeField(verbose_name='Date and Time')),
                ('incident_loaction', models.TextField(help_text='where did it happend in the company', verbose_name='Incident Location')),
                ('severity', models.CharField(choices=[('1', 'Mild'), ('2', 'Moderate'), ('3', 'Severe'), ('4', 'Fatal')], default='1', max_length=100, verbose_name='Initial severit')),
                ('cause', models.TextField(verbose_name='Suspected Cause')),
                ('action_taken', models.TextField(verbose_name='immediate action taken')),
                ('environmental', models.BooleanField(default=False, verbose_name='Enviromental Incident')),
                ('injury_illnes', models.BooleanField(default=False, verbose_name='Injury/Illnes')),
                ('property_damage', models.BooleanField(default=False, verbose_name='Property Damage')),
                ('vehicle', models.BooleanField(default=False, verbose_name='Vehicle')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Reported By')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 's',
            },
        ),
    ]
