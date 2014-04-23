from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from vending.models import Round, Manufacturer, Cartridge, Material, Caliber, Bullet
#from vending.models import Round, Caliber, Purpose, Weapon, Company

def caliber_changed(request):
    u''' Handles an event in the form of a "caliber" selection change.
    '''
    context = {'action' : 'success', 
               'message': 'Caliber changed!',} 
    return context;

def bullet_changed(request):
    u''' Handles an event in the form of a "purpose" selection change.
    '''
    context = {'action' : 'success', 
               'message': 'Bullet changed!',} 
    return context;



def manufacturer_changed(request):
    u''' Handles an event in the form of a "company" selection change.
    '''
    context = {'action' : 'success', 
               'message': 'Manufacturer changed!',} 
    return context;



def material_changed(request):
    u''' Handles an event in the form of a "weapon" selection change.
    '''
    context = {'action' : 'success', 
               'message': 'Material changed!',} 
    return context;




