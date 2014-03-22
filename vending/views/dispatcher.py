from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.template import RequestContext, loader
from django.http import Http404

from vending.models import Round, Caliber, Purpose, Weapon, Company

from vending.views import ajax


# Create your views here.
def index(request):
    u''' Delegates the responsibility of rendering the template 
         "vending/index.html" to appropriate request handlers.
    '''

    company_list = Company.objects.all()
    purpose_list = Purpose.objects.all()
    weapon_list = Weapon.objects.all()
    caliber_list = Caliber.objects.all()
    round_list = Round.objects.all()

    if request.is_ajax():
        if 'update' in request.GET:
            response = ajax.handle_update( request )
        return HttpResponse( response, content_type='application/json' )            


    context = {'round_list': round_list,
               'caliber_list':caliber_list,
               'purpose_list': purpose_list,
               'weapon_list':weapon_list,
               'company_list':company_list,}
    return render(request, 'vending/index.html', context)


def detail(request, round_id):
    round = get_object_or_404(Round, pk=round_id)
    return render(request, 'vending/detail.html', {'round': round})


