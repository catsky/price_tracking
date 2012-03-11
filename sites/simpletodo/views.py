#!/usr/bin/env python
# coding: utf-8
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages

from models import Product

class AddForm(forms.ModelForm):
    productLink = forms.CharField(label='请输入Amazon商品地址')
    class Meta:
        model = Product
        fields = ('productLink',)

class TrackForm(forms.ModelForm):
    productLink = forms.CharField(label='跟踪的商品地址', required=False)
    productName = forms.CharField(label='商品名称', required=False)
    star = forms.CharField(label='商品评级', required=False)
    feature = forms.CharField(label='商品特性', required=False)
    details = forms.CharField(label='商品详情', required=False)
    originPrice = forms.CharField(label='原价', required=False)
    currentPrice = forms.CharField(label='现价', required=False)
    crawlDate = forms.DateTimeField(label='抓取时间', required=False)
    inStock = forms.CharField(label='有货', required=False)
    firstCommentDate = forms.DateTimeField(label='第一次评论时间', required=False)
    firstComment = forms.CharField(label='第一次评论', required=False)
    secondCommentDate = forms.DateTimeField(label='第二次评论时间', required=False)
    secondComment = forms.CharField(label='第二次评论', required=False)
    thirdCommentDate = forms.DateTimeField(label='第三次评论时间', required=False)
    thirdComment = forms.CharField(label='第三次评论', required=False)
    imageLink = forms.CharField(label='图像', required=False)
    class Meta:
        model = Product



def index(request):
    ctx = {}
    ctx['todos'] = Product.objects.all().order_by('-id')
    ctx['form'] = AddForm()
    return render(request, 'index.html', ctx)

def new(request):
    form = AddForm()
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            todo = Product(productLink=request.POST['productLink'])
            trackForm = TrackForm(instance=todo)
	    return render(request, 'todo/add_track.html', {'form': trackForm})
    return render(request, 'todo/add_track.html', {'form': form})

def addTrack(request):
    trackForm = TrackForm()
    if request.method == "POST":
        trackForm = TrackForm(request.POST)
        if trackForm.is_valid():
            trackForm.save()
            messages.info(request, u'跟踪成功')
            return HttpResponseRedirect(reverse("todo_idx"))
    return render(request, 'todo/add_track.html', {'form': trackForm})

def edit(request, id):
    edit_todo = get_object_or_404(Product, id=id)
    form = TrackForm(instance=edit_todo)
    if request.method == "POST":
        form = TrackForm(request.POST, instance=edit_todo)
        if form.is_valid():
            form.save()
            messages.info(request, u'编辑成功')
            return HttpResponseRedirect(reverse("todo_idx"))
    return render(request, 'todo/form.html', {'form': form})

def delete(request, id):
    todo = get_object_or_404(Product, id=id)
    todo.delete()
    messages.info(request, u'成功删除')
    return HttpResponseRedirect(reverse("todo_idx"))

