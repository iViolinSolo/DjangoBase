#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: violinsolo
# Created on 30/07/2017

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world ! ")


def hello_world(request):
    context = {}
    context['hello_text'] = 'Hello World! Honey!'

    return render(request=request, template_name='demo/hello.html', context=context)