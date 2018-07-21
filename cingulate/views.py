# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db import transaction
from models import *


@transaction.atomic
def get_project_vo(request):
    o_project = Project.objects.all()[0]
    # o_suite = Suite.objects.all()[0]

    context = dict()
    context['project'] = o_project
    # o_suite.project.name = "openapi"
    # o_suite.project.save()
    return render(request, 'projects.html', context)
