#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from django.shortcuts import render,redirect
def hello(request):
    # context          = {}
    # context['hello'] = 'Hello World!'
    # context['world'] = 'haha'
    # return render(request, 'hello.html', context)
    return redirect('http://localhost:8080/jikeng')