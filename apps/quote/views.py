# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
    context = {
        "quotes": quote.objects.filter(users=request.session['uid']),
        "allq": quote.objects.exclude(users = request.session['uid'])
        }
    return render(request, "quote/index.html", context)

def makequote(request):
    if request.method == "POST":
        errors = quote.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/quotes')
        else:
            quote.objects.create(author=request.POST['author'], quote = request.POST['quote'], user_id=request.session['uid'])
            return redirect('/quotes')
    else:
        return redirect('/quotes')

def results(request):
    return render(request, "login/results.html")

def addfav(request):
    this_quote = quote.objects.get(id=request.POST['quote_id'])
    this_user = user.objects.get(id=request.session['uid'])
    this_quote.users.add(this_user)
    return redirect('/quotes')

def remfav(request):
    this_quote = quote.objects.get(id=request.POST['quote_id'])
    this_user = user.objects.get(id=request.session['uid'])
    #quote.users.filter(this_quote, this_user) 
    this_quote.users.remove(this_user)
    return redirect('/quotes')

def dashboard(request,user_no):
    context = {
        "quotes": quote.objects.filter(user_id=user_no),
        "user_data": user.objects.get(id = user_no)
    }
    return render(request, "quote/results.html", context)