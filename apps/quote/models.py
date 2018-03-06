# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login.models import user

class quoteManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['author']) < 4:
            errors["fname"] = "Name should be more than 3 characters"
        if len(postData['quote']) < 11:
            errors["aname"] = "Quote should be more than 10 characters"
        return errors
    
class quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField(max_length=1000, default="none")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    users = models.ManyToManyField(user, related_name="favs")
    user = models.ForeignKey(user, related_name="posted_by", default=0)
    objects = quoteManager()