# Generated by Django 2.1.2 on 2018-12-12 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcore', '0003_application_ready'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='package_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
