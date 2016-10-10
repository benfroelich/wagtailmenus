# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmenus', '0011_auto_20160415_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatmenuitem',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page', verbose_name='link to an internal page'),
        ),
        migrations.AlterField(
            model_name='flatmenuitem',
            name='link_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='link to a custom URL'),
        ),
        migrations.AlterField(
            model_name='flatmenuitem',
            name='url_append',
            field=models.CharField(blank=True, help_text="Use this to optionally append a #hash or querystring to the above page's URL.", max_length=255, verbose_name='append to URL'),
        ),
        migrations.AlterField(
            model_name='mainmenu',
            name='site',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='main_menu', to='wagtailcore.Site'),
        ),
        migrations.AlterField(
            model_name='mainmenuitem',
            name='allow_subnav',
            field=models.BooleanField(default=True, verbose_name='allow sub-navigation for this page'),
        ),
        migrations.AlterField(
            model_name='mainmenuitem',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page', verbose_name='link to an internal page'),
        ),
        migrations.AlterField(
            model_name='mainmenuitem',
            name='link_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='link to a custom URL'),
        ),
        migrations.AlterField(
            model_name='mainmenuitem',
            name='url_append',
            field=models.CharField(blank=True, help_text="Use this to optionally append a #hash or querystring to the above page's URL.", max_length=255, verbose_name='append to URL'),
        ),
    ]
