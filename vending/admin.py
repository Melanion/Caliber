from django.contrib import admin
from vending.models import Round
from vending.models import Caliber
from vending.models import Manufacturer
from vending.models import Material
from vending.models import Bullet
from vending.models import Cartridge


# Register your models here.
admin.site.register(Round)
admin.site.register(Caliber)
admin.site.register(Manufacturer)
admin.site.register(Material)
admin.site.register(Bullet)
admin.site.register(Cartridge)
