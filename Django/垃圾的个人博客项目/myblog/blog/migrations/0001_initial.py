# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '评论表',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=50)),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='内容')),
                ('img', models.ImageField(upload_to='')),
                ('pub_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('modify_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('source', models.CharField(verbose_name='来源', max_length=50)),
                ('look', models.IntegerField(verbose_name='围观次数', default=0)),
                ('zan', models.IntegerField(verbose_name='点赞数', default=0)),
                ('adv', models.BooleanField(verbose_name='广告位', default=False)),
                ('classify', models.CharField(verbose_name='分类', max_length=50, choices=[('网站前端', '网站前端'), ('后端技术', '后端技术')])),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': '每日一句',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
