# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
    #request.session['counter'] = 1
    return render(request, "login/index.html")

def create(request):
    if request.method == "POST":
        errors = user.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            pass_hash = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt())
            user.objects.create(name=request.POST['name'], alias = request.POST['alias'],email_address = request.POST['email_address'], password=pass_hash  )
            return redirect('/register', { "user_data": user.objects.get(email_address = request.POST['email_address']) })
    else:
        return redirect('/')

def results(request):
    return render(request, "login/results.html")

def register(request):
    return render(request, "login/register.html")

def login(request):
    errors = user.objects.login_try(request.POST)  
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/')        
    else:
        errors = user.objects.pw_match(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
                return redirect('/')   
        else:
            con = {
            "user_data": user.objects.get(email_address = request.POST['login_address'])
            }
            user_info = user.objects.get(email_address = request.POST['login_address'])
            request.session['uid'] = user_info.id
            request.session['alias'] = user_info.alias
            user_no = request.session['uid']
            return redirect("/quotes")

def logout(request):
    del request.session['uid']
    del request.session['alias']
    return redirect('/')
