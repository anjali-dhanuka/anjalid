# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
   user = models.OneToOneField(User)
   score = models.IntegerField(default=0)

   













# Create your models here.
