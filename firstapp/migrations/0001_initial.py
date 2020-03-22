# Generated by Django 3.0.2 on 2020-01-26 14:19

import datetime
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
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('describe', models.TextField(default='qwerty')),
                ('caseimg', models.ImageField(upload_to='images')),
                ('img1', models.ImageField(upload_to='images')),
                ('nam1', models.CharField(default='qwerty', max_length=40)),
                ('img2', models.ImageField(upload_to='images')),
                ('nam2', models.CharField(default='qwerty', max_length=40)),
                ('img3', models.ImageField(upload_to='images')),
                ('nam3', models.CharField(default='qwerty', max_length=40)),
                ('img4', models.ImageField(upload_to='images')),
                ('nam4', models.CharField(default='qwerty', max_length=40)),
                ('img5', models.ImageField(upload_to='images')),
                ('nam5', models.CharField(default='qwerty', max_length=40)),
                ('img6', models.ImageField(upload_to='images')),
                ('nam6', models.CharField(default='qwerty', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mydate', models.DateTimeField(default=datetime.datetime(2020, 4, 25, 14, 19, 33, 373008))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Profile')),
            ],
        ),
    ]