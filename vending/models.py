from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Caliber(models.Model):
    name = models.CharField(max_length=50)
    weapon_type = models.ForeignKey(Weapon)

    def __unicode__(self):
        return self.name

class Purpose(models.Model):
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return self.description

class Round(models.Model):
    name = models.CharField(max_length=50)
    caliber = models.ForeignKey(Caliber)
    purpose = models.ForeignKey(Purpose)
    year = models.IntegerField(max_length=2)
    manufacturer = models.ForeignKey(Company)

    def __unicode__(self):
        return self.name
