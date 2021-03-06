# Generated by Django 3.0.8 on 2020-07-19 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0006_auto_20200711_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('website_url', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
