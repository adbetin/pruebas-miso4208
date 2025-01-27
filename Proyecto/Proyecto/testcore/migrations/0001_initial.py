# Generated by Django 2.1.1 on 2018-09-19 06:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, max_length=500)),
                ('repositoryUrl', models.URLField(blank=True, max_length=500)),
                ('apphash', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('value', models.TextField()),
                ('testhash', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('status', models.CharField(choices=[('No ejecutado', 'NOTRUN'), ('Iniciado', 'START'), ('Progreso', 'PROGRESS'), ('Exitosa', 'SUCCESS'), ('Fallida', 'FAIL'), ('No definido', 'UNDEFINED')], default='No ejecutado', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='applicationTests', to='testcore.Application')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('command', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestExecution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('No ejecutado', 'NOTRUN'), ('Iniciado', 'START'), ('Progreso', 'PROGRESS'), ('Exitosa', 'SUCCESS'), ('Fallida', 'FAIL'), ('No definido', 'UNDEFINED')], default='No ejecutado', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('started_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('finished_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('reportText', models.TextField()),
                ('applicationTest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='testExecutions', to='testcore.ApplicationTest')),
            ],
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='library',
            name='testType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='libraries', to='testcore.TestType'),
        ),
        migrations.AddField(
            model_name='applicationtest',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='libraries', to='testcore.Library'),
        ),
        migrations.AddField(
            model_name='applicationtest',
            name='testType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appTests', to='testcore.TestType'),
        ),
        migrations.AddField(
            model_name='application',
            name='applicationType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='applications', to='testcore.ApplicationType'),
        ),
    ]
