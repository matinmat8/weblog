# Generated by Django 4.2.2 on 2023-06-26 07:12

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('publish', models.DateTimeField()),
                ('draft_note', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.CharField(max_length=150, unique_for_date='publish')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=60)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
