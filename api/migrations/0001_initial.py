# Generated by Django 2.2 on 2019-12-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
