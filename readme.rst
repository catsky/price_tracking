=======================
amazon price track (Django 版)
=======================

缘起
====
在中国，海淘日益流行，特别是在amazon上购物成了广大淘友的最爱。如何跟踪那些即时打折的商品让网友不再错过好的宝贝，这是开发这个项目的初衷。

我也是一个python的初学者，step by step 构建我们的应用.

运行需求
========
Django>=1.3

安装及运行
==========

初始化数据库：
python manage.py syncdb

启动：
python manage.py runserver

使用：
在浏览器中打开 http://127.0.0.1:8000/

Django Admin:
在浏览器中打开 http://127.0.0.1:8000/admin/

项目开发记录
============

#. 创建django project和app::

    django-admin.py startproject 3haitao 
    cd 3haitao/
    python manage.py startapp 3haitao 

#. 编辑settings.py完成数据库、模板、静态文件等配置，主要配置条目::

    #注：我认为django应当加更多的默认设置，这些配置改的挺烦
    DATABASES
    INSTALLED_APPS
    STATIC_ROOT
    STATICFILES_DIRS
    TEMPLATE_DIRS

#. 编辑urls.py把django admin和static文件url配置加上。

#. 编辑simpletodo/models.py，完成数据模型::

    from django.db import models
    from django.contrib import admin

    class Todo(models.Model):
        title = models.CharField( max_length=255)
        finished = models.IntegerField(default=0)

        def __unicode__(self):
            return self.title

#. 创建数据库::

    python manage.py syncdb

#. 跑起来，进django admin看看先::

    python manage.py runserver
    #http://127.0.0.1:8000/admin/
    
#. 接下来，略...
