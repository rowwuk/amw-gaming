# Generated by Django 2.2.17 on 2020-12-04 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('doors', models.IntegerField()),
            ],
        ),
    ]
