# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Portion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(max_length=15)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portions', to='solawi.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Potential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='potentials', to='solawi.Portion')),
            ],
        ),
        migrations.CreateModel(
            name='Swap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swpas', to='solawi.Portion')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solawi.Portion')),
            ],
        ),
        migrations.CreateModel(
            name='TimedPotential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('portion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timedpotentials', to='solawi.Portion')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='The persons first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='The persons last name')),
                ('mail', models.EmailField(max_length=254, verbose_name='The persons E-Mail address')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='solawi.User')),
            ],
            bases=('solawi.user',),
        ),
        migrations.CreateModel(
            name='DepotHead',
            fields=[
                ('member_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='solawi.Member')),
            ],
            bases=('solawi.member',),
        ),
        migrations.AddField(
            model_name='timedpotential',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timedpotentials', to='solawi.Member'),
        ),
        migrations.AddField(
            model_name='potential',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='potentials', to='solawi.Member'),
        ),
        migrations.AddField(
            model_name='member',
            name='depot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='solawi.Depot'),
        ),
    ]
