# Generated by Django 2.2.2 on 2019-06-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ns_id', models.CharField(max_length=150)),
                ('vnf_member_index', models.IntegerField()),
                ('scaling_group_descriptor', models.CharField(max_length=150)),
                ('cooldown_period', models.FloatField()),
                ('vdu_count', models.IntegerField()),
                ('cpu_load', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
