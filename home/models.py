# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    funcion = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Parcela(models.Model):

    #__Parcela_FIELDS__
    nomenclatura = models.CharField(max_length=255, null=True, blank=True)
    titular = models.CharField(max_length=255, null=True, blank=True)
    id_areas = models.ForeignKey(Area, on_delete=models.CASCADE)

    #__Parcela_FIELDS__END

    class Meta:
        verbose_name        = _("Parcela")
        verbose_name_plural = _("Parcela")


class Area(models.Model):

    #__Area_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    estado_area = models.CharField(max_length=255, null=True, blank=True)

    #__Area_FIELDS__END

    class Meta:
        verbose_name        = _("Area")
        verbose_name_plural = _("Area")


class Empresa(models.Model):

    #__Empresa_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    estado_empresa = models.CharField(max_length=255, null=True, blank=True)
    id_areas = models.ForeignKey(Area, on_delete=models.CASCADE)

    #__Empresa_FIELDS__END

    class Meta:
        verbose_name        = _("Empresa")
        verbose_name_plural = _("Empresa")



#__MODELS__END
