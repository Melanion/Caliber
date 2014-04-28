from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.template import RequestContext, loader
from django.http import Http404

from vending.models import Round, Manufacturer, Cartridge, Material, Caliber, Bullet
from vending.views import ajax

import json

# Create your views here.
def index(request):
    u''' Delegates the responsibility of rendering the template 
         "vending/index.html" to appropriate request handlers.
    '''

    if request.is_ajax():
        if 'update' in request.GET:
            response = ajax.handle_update( request )
            print "???"
        return HttpResponse( response, content_type='application/json' )            


    cartridges = Cartridge.objects.all();
    results = Round.objects.filter( cartridge = cartridges );

    
    context = {'results': results,
               'caliber_list' : Caliber.objects.all(),
               'bullet_list' : Bullet.objects.all(),
               'manufacturer_list' : Manufacturer.objects.all(),
               'material_list' : Material.objects.all(),
               }
    
    return render(request, 'vending/index.html', context)


def detail(request, round_id):
    round = get_object_or_404(Round, pk=round_id)
    return render(request, 'vending/detail.html', {'round': round})


def round_details(request, round_id):
    round = get_object_or_404(Round, pk=round_id)
    return render(request, 'vending/round_details.html', {'round': round})


def cartridge_details(request, cartridge_id):
    cartridge = get_object_or_404(Cartridge, pk=round_id)
    return render(request, 'vending/cartridge_details.html', {'round': cartridge})


def manufacturer_details(request, mfgr_id):
    manufacturer = get_object_or_404(Manufacturer, pk=mfgr_id)
    return render( request, 
                   'vending/manufacturer_details.html', 
                   {'manufacturer':manufacturer})



def about(request):
    return render(request, 'vending/about.html')


