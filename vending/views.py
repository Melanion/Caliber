from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from vending.models import Round

# Create your views here.
def index(request):
    round_list = Round.objects.all()
    context = {'round_list': round_list}
    return render(request, 'vending/index.html', context)
