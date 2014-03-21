from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from vending.models import Round, Caliber, Purpose, Weapon, Company

# Create your views here.
def index(request):
    
    company_list = Company.objects.all()
    purpose_list = Purpose.objects.all()
    weapon_list = Weapon.objects.all()
    caliber_list = Caliber.objects.all()
    round_list = Round.objects.all()
    context = {'round_list': round_list, 
               'caliber_list':caliber_list,
               'purpose_list': purpose_list,
               'weapon_list':weapon_list,
               'company_list':company_list,}
    return render(request, 'vending/index.html', context)
