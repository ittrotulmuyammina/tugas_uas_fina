from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def wisata(request):
  template = loader.get_template('wisata.html')
  return HttpResponse(template.render())
def coba(request):
  template = loader.get_template('coba.html')
  return HttpResponse(template.render())

def base(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())
def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())


