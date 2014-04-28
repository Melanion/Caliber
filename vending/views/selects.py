from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from vending.models import Round, Manufacturer, Cartridge, Material, Caliber, Bullet

def caliber_changed(request):
    u''' Handles an event in the form of a "caliber" selection change.
    '''

    if 'caliber' in request.GET:
        request.session['caliber'] = request.GET['action']
    else:
        request.session['caliber'] = 'any'
    print request.session['caliber']
    

def bullet_changed(request):
    u''' Handles an event in the form of a "purpose" selection change.
    '''
    if 'bullet' in request.GET:
        request.session['bullet'] = request.GET['action']
    else:
        request.session['bullet'] = 'any'


def manufacturer_changed(request):
    u''' Handles an event in the form of a "manufacturer" selection change.
    '''
    if 'manufacturer' in request.GET:
       request.session['manufacturer'] = request.GET['action']
    else:
        request.session['manufacturer'] = 'any'


def material_changed(request):
    u''' Handles an event in the form of a "material" selection change.
    '''
    if 'material' in request.GET:
        request.session['material'] = request.GET['action']
    else:
        request.session['material'] = 'any'
