# encoding: utf-8

from django.contrib.sites.models import Site

def sites(request):
    return {'site':Site.objects.get_current(), }