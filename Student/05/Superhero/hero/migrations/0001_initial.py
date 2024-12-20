# Generated by Django 4.2.4 on 2024-12-06 10:35

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
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('identity', models.CharField(max_length=200)),
                ('description', models.TextField(default='None')),
                ('image', models.CharField(default='None', max_length=200)),
                ('strengths', models.CharField(default='None', max_length=200)),
                ('weaknesses', models.CharField(default='None', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
