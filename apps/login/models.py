# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
import bcrypt

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        uwe = user.objects.filter(email_address = postData['email_address'])
        if len(postData['name']) < 3:
            errors["fname"] = "Name should be more than 2 characters"
        if not (postData['name']).isalpha():
            errors["fnamel"] = "Name can only be characters"
        if len(postData['alias']) < 3:
            errors["aname"] = "Alias should be more than 2 characters"
        if not postData['alias'].isalpha():
            errors["fnamel"] = "Alias can only be characters"
        try:
            validate_email(postData['email_address'])
        except ValidationError as e:
           errors["email"] = "Email must be valid"
        if len(uwe) > 0:
            errors["exists"] = "Already registered. Click nowhere to recover passowrd."
        if len(postData['pass']) < 8:
            errors["pass_l"] = "Password must be 8 characters"
        if (postData['pass'] !=  postData['c_pass']):
            errors["pass_m"] = "Password fields must match"
        return errors
    def login_try(self, postData):
        errors = {}
        try:
            user.objects.get(email_address = postData['login_address']) 
            return errors
        except:
            errors["email"] = "Email not in DB"
            return errors
    def pw_match(self, postData):
        errors = {}
        usr = user.objects.get(email_address = postData['login_address'])
        usr_pw = usr.password
        post_pw=postData['pw']
        if bcrypt.checkpw(post_pw.encode(), usr_pw.encode()): 
            return errors
        else:
            errors["email"] = "Wrong password"
            return errors

class user(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = userManager()