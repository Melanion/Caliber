from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    ''' 
    '''
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=16);    

    def __unicode__(self):
        return self.name

class Bullet(models.Model):
    purpose = models.CharField(max_length=32)

    def __unicode__(self):
        return self.purpose

class Caliber(models.Model):
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return self.description

class Cartridge(models.Model):
    rimfire = models.BooleanField(default=1)
    
    caliber = models.ForeignKey(Caliber)
    material = models.ForeignKey(Material)
    bullet = models.ForeignKey(Bullet)

class Round(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField( max_digits=5, decimal_places=2);
    inventory_count = models.IntegerField(max_length=4)

    manufacturer = models.ForeignKey(Manufacturer)
    cartridge = models.ForeignKey( Cartridge ); 

    def __unicode__(self):
        return self.name
