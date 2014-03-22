from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from vending.models import Round, Caliber, Purpose, Weapon, Company

def caliber_changed(request):
    u''' Handles an event in the form of a caliber selection change.
    '''
    context = {'message': 'Caliber changed!',} 
    return render(request, 'vending/testbed.html', context)

def purpose_changed(request):
    u'''
    '''
    context = {'round_': round_list,} 
    context = {'message': 'Purpose changed!',} 
    return render(request, 'vending/testbed.html', context)

def company_changed(request):
    u'''
    '''
    context = {'message': 'Company changed!',} 
    return render(request, 'vending/testbed.html', context)


def weapon_changed(request):
    u'''
    '''
    context = {'message': 'Weapon changed!',} 
    return render(request, 'vending/testbed.html', context)



