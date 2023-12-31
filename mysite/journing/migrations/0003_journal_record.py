# Generated by Django 4.2.2 on 2023-08-27 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traveldata', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('journing', '0002_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(default='Untitled')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traveldata.cities')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': '"journingdata"."journal"',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_uuid', models.UUIDField()),
                ('hour', models.SmallIntegerField(default=None)),
                ('remark', models.CharField(default=None, max_length=1000)),
                ('date', models.DateField(default=None, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journing.journal')),
            ],
            options={
                'db_table': '"journingdata"."record"',
            },
        ),
    ]
