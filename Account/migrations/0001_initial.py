#  Copyright (c) 2021.  TheFox

# Generated by Django 3.1.7 on 2021-04-27 17:08

import django.db.models.deletion
import smart_selects.db_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Educational_organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='образовательная организация')),
                ],
            ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='населённый пункт')),
                ],
            ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='городской округ / Муниципальный район')),
                ],
            ),
        migrations.CreateModel(
            name='Type_of_oo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='тип ОО')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.locality', verbose_name='населённый пункт')),
                ],
            ),
        migrations.AddField(
            model_name='locality',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.place', verbose_name='городской округ / Муниципальный район'),
            ),
        migrations.CreateModel(
            name='Giseo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=150, verbose_name='логин')),
                ('password', models.CharField(max_length=100, verbose_name='пароль')),
                ('educational_organization', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='type_of_oo', chained_model_field='type_of_oo',
                                                                                       on_delete=django.db.models.deletion.CASCADE, to='Account.educational_organization',
                                                                                       verbose_name='образовательная организация')),
                ('locality',
                 smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='place', chained_model_field='place', on_delete=django.db.models.deletion.CASCADE,
                                                           to='Account.locality', verbose_name='населённый пункт')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.place', verbose_name='городской округ / Муниципальный район')),
                ('type_of_oo',
                 smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='locality', chained_model_field='locality', on_delete=django.db.models.deletion.CASCADE,
                                                           to='Account.type_of_oo', verbose_name='тип ОО')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
                ],
            options={
                'verbose_name': 'giseo',
                'verbose_name_plural': "giseo's",
                'ordering': ['user', 'login', 'place'],
                'managed': True,
                },
            ),
        migrations.AddField(
            model_name='educational_organization',
            name='type_of_oo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.type_of_oo', verbose_name='тип ОО'),
            ),
        ]
