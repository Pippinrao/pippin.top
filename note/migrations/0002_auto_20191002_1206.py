# Generated by Django 2.2.2 on 2019-10-02 04:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(default=datetime.datetime(2019, 10, 2, 12, 6, 38, 399501))),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(default=datetime.datetime(2019, 10, 2, 12, 6, 38, 399501))),
            ],
        ),
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 2, 12, 6, 38, 400499)),
        ),
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note', to='note.Category'),
        ),
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='note', to='note.Tag'),
        ),
    ]