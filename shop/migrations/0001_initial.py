# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models, migrations
import filer.fields.file


class Migration(migrations.Migration):

    AUTH_APP_LABEL = ".".join([
        "{}".format(v).lower() for v in settings.AUTH_USER_MODEL.split('.')[:-1]])

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('post_office', '0002_add_i18n_and_backend_alias'),
        (AUTH_APP_LABEL, '0001_initial'),
    ]

    customer_bases = (settings.AUTH_USER_MODEL.lower(),)

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('transition_target', models.CharField(max_length=50, verbose_name='Event')),
                ('mail_to', models.PositiveIntegerField(default=None, null=True, verbose_name='Mail to', blank=True)),
                ('mail_template', models.ForeignKey(verbose_name='Template', to='post_office.EmailTemplate', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NotificationAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attachment', filer.fields.file.FilerFileField(related_name='email_attachment', blank=True, to='filer.File', null=True)),
                ('notification', models.ForeignKey(to='shop.Notification', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CustomerProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Customer',
                'proxy': True,
                'verbose_name_plural': 'Customers',
            },
            bases=customer_bases,
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('post_office.email',),
        ),
    ]
