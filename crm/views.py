# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request,'index.html')

@login_required
def table_obj_list():
    pass

