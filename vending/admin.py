from django.contrib import admin
from vending.models import Round
from vending.models import Caliber
from vending.models import Company
from vending.models import Purpose
from vending.models import Weapon

# Register your models here.
admin.site.register(Round)
admin.site.register(Caliber)
admin.site.register(Company)
admin.site.register(Purpose)
admin.site.register(Weapon)
