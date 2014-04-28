import json

from django.core import serializers

from vending.views import selects
from vending.models import Cartridge, Round, Bullet, Material, Caliber, Manufacturer

def handle_update(request):

    field = request.GET.get('update', 'none')
    request.session[field] = request.GET.get( 'value', 'any' )
    
    results = Round.objects.all()
    cartridge = Cartridge.objects.all()
    manufacturer = Manufacturer.objects.all()

    bullet = Bullet.objects.all()
    if 'any' != get_value( request, 'bullet' ):
        bullet = Bullet.objects.filter( pk = get_value(request, 'bullet') )

    caliber = Caliber.objects.all()
    if 'any' != get_value( request, 'caliber' ):
        caliber = caliber.filter( pk = get_value(request, 'caliber') )

    material = Material.objects.all()
    if 'any' != get_value( request, 'material' ):
        material = Material.objects.filter( pk = get_value(request, 'material') )

    cartridge = cartridge.filter( bullet=bullet, 
                                  caliber=caliber, 
                                  material=material)

    results = results.filter( cartridge=cartridge, manufacturer=manufacturer ) 

    
    context = {'action' : 'success', 
               'results' : serializers.serialize('xml', results), }

    print caliber

    return json.dumps( context );

    

def get_value(request, field):
    request.session[field] = request.session.get( field, 'any' )
