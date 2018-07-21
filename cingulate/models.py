# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)


class Suite(models.Model):
    project = models.ForeignKey(Project)
    number = models.IntegerField()
    name = models.CharField(max_length=50)
