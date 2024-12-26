# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from calendar import c
from pyexpat import model

import random
import string

from unittest.util import _MAX_LENGTH
from django.db import models

from django.core.files.storage import FileSystemStorage

from django.conf import settings
User = settings.AUTH_USER_MODEL

from django.urls import reverse
from django.utils.text import slugify

from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from rest_framework.authtoken.models import Token

class CustomToken(Token):
    expires_at = models.DateTimeField(null=True, blank=True)
    

    class Meta:
        db_table = 'custom_token'

class Rol(models.Model):
      id = models.AutoField(primary_key=True)
      Name=models.CharField(max_length=20)
      created=models.DateField(auto_now_add=True)
      updated=models.DateField(auto_now_add=True)
      class Meta:
            verbose_name="Rol"
            verbose_name_plural="Roles"
      def __str__(self):
            return self.Name

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    roles =models.ManyToManyField(Rol)
    direccion=models.CharField(max_length=10,null=True)


class Inquilino(models.Model):
    # datos personales
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    p_fom=models.CharField(max_length=100, blank=True)
    nombre=models.CharField(max_length=100, blank=True)
    apellido= models.CharField(max_length=100, null=True, blank=True)
    apellido1=models.CharField(max_length=100, null=True, blank=True)
    rfc=models.CharField(max_length=13, null=True, blank=True)
    estado_civil=models.CharField(max_length=100,null=True, blank=True)
    n_conyuge=models.CharField(max_length=100, null=True, blank=True)
    a_conyuge=models.CharField(max_length=100, null=True, blank=True)
    a1_conyuge=models.CharField(max_length=100, null=True, blank=True)    
    numeroTel=models.BigIntegerField(null=True, blank=True) 
    numeroTel1=models.BigIntegerField(null=True, blank=True) 
    email=models.EmailField()
    nacionalidad=models.CharField(max_length=100, null=True, blank=True, default="Mexicana")
   
    # datos domiciliarios
    calle=models.CharField(max_length=100, null=True, blank=True)
    num_ext=models.CharField(max_length=100,null=True, blank=True)
    num_int=models.CharField(max_length=100,null=True, blank=True, default=0)
    colonia=models.CharField(max_length=100, null=True, blank=True)
    estado=models.CharField(max_length=100, null=True, blank=True)
    codigopostal=models.BigIntegerField(null=True, blank=True)
    municipio_alcaldia=models.CharField(max_length=100, null=True, blank=True)
    referencias=models.CharField(max_length=100, null=True, blank=True)
    
    #Datos Empleo
    profesion=models.CharField(max_length=100, null=True, blank=True)
    antiguedad=models.BigIntegerField(null=True, blank=True)
    puesto=models.CharField(max_length=100, null=True, blank=True)
    tel_empleo=models.BigIntegerField(null=True, blank=True)
    ingreso_men=models.BigIntegerField(null=True, blank=True)
    nombre_empresa=models.CharField(max_length=100, null=True, blank=True)
    email_empresarial=models.EmailField(null=True, blank=True)
    cel_empleo=models.BigIntegerField(null=True, blank=True)
    
    #Jefe
    jefe=models.CharField(max_length=100, null=True, blank=True)
    puesto_jefe=models.CharField(max_length=100, null=True, blank=True)
    pagina_web=models.CharField(max_length=100, null=True, blank=True)
    giro=models.CharField(max_length=100, null=True, blank=True)
    tel_jefe=models.BigIntegerField(null=True, blank=True)
    email_jefe=models.EmailField(null=True, blank=True)

    #acta constitutiva
    empresa_constituida = models.CharField(max_length=50, null=True, blank=True)
    escritura_numero_ac = models.CharField(max_length=50, null=True, blank=True)
    fecha_ac = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    nombre_notario_ac = models.CharField(max_length=50, null=True, blank=True)
    coe = models.CharField(max_length=100, null=True, blank=True)
    folio_mercantil = models.BigIntegerField(null=True, blank=True)

    #Direccion empleo
    calle_empleo=models.CharField(max_length=60, null=True, blank=True)
    num_ext_empleo=models.CharField(max_length=100,null=True, blank=True)
    num_int_empleo=models.CharField(max_length=100,null=True, blank=True, default=0)
    colonia_empleo=models.CharField(max_length=100,null=True, blank=True)
    ciudad_empleo=models.CharField(max_length=100, null=True, blank=True)
    codigo_postal_empleo=models.BigIntegerField(null=True, blank=True)
    municipio_empleo=models.CharField(max_length=100, null=True, blank=True)
    
    # Referencia del Arrendatario Anterior
    rentado_antes=models.CharField(max_length=2, null=True, blank=True)
    nombre_aa=models.CharField(max_length=100, null=True, blank=True)
    monto_renta_aa=models.BigIntegerField(null=True, blank=True)
    telefono_aa=models.BigIntegerField(null=True, blank=True)
    motivo_cambio=models.CharField(max_length=100, null=True, blank=True)
    renta_compartida = models.CharField(max_length=2, null=True, blank=True)
    no_renta_compartida = models.CharField(max_length=5, null=True, blank=True)
    #Dom Inmueble Arrendado
    calle_dia=models.CharField(max_length=100, null=True, blank=True)
    num_ext_dia=models.CharField(max_length=100,null=True, blank=True)
    num_int_dia=models.CharField(max_length=100,null=True, blank=True, default=0)
    colonia_dia=models.CharField(max_length=100,null=True, blank=True)
    ciudad_dia=models.CharField(max_length=100, null=True, blank=True)
    codigo_postal_dia=models.BigIntegerField(null=True, blank=True)
    municipio_dia=models.CharField(max_length=100, null=True, blank=True)
    
    # Referencias Personales
    n_ref1=models.CharField(max_length=100, null=True, blank=True)
    p_ref1=models.CharField(max_length=100, null=True, blank=True)
    tel_ref1=models.BigIntegerField(null=True, blank=True)
    n_ref2=models.CharField(max_length=100, null=True, blank=True)
    p_ref2=models.CharField(max_length=100, null=True, blank=True)
    tel_ref2=models.BigIntegerField(null=True, blank=True)
    n_ref3=models.CharField(max_length=100, null=True, blank=True)
    p_ref3=models.CharField(max_length=100, null=True, blank=True)
    tel_ref3=models.BigIntegerField(null=True, blank=True)
    
    # Inquilinos
    no_inquilinos = models.BigIntegerField(null=True, blank=True)
    n_inquilino1=models.CharField(max_length=100, null=True, blank=True)
    p_inquilino1=models.CharField(max_length=100, null=True, blank=True)
    n_inquilino2=models.CharField(max_length=100, null=True, blank=True)
    p_inquilino2=models.CharField(max_length=100, null=True, blank=True)
    n_inquilino3=models.CharField(max_length=100, null=True, blank=True)
    p_inquilino3=models.CharField(max_length=100, null=True, blank=True)
    n_inquilino4=models.CharField(max_length=100, null=True, blank=True)
    p_inquilino4=models.CharField(max_length=100, null=True, blank=True)
    n_inquilino5=models.CharField(max_length=100, null=True, blank=True)
    p_inquilino5=models.CharField(max_length=100, null=True, blank=True)
    
    tyc = models.CharField(max_length=100, null=True, blank=True)
    tarjeta  =  models.JSONField(null=True)
    credito  =  models.JSONField(null=True)
    
    mi_agente_es = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    codigo_amigo = models.CharField(max_length=8, editable = False, unique=True)
    created = models.DateField(auto_now_add=True, null=True, blank=True)
      
    def save(self, *args, **kwargs):
        characters = string.ascii_letters + string.digits
        length = 4
        name = str(self.nombre[0:2])
        print(characters)
        print(name)
        self.codigo_amigo = 'AR' + ''.join(random.choice(characters) for _ in range(length)) + name.upper()
        print(self.codigo_amigo)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.apellido1}'
    
    class Meta:
        db_table = 'inquilinos'



class Fiador_obligado(models.Model):
    # fiador/oblicado
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    inquilino = models.ForeignKey(Inquilino, null=True, blank=True, on_delete=models.CASCADE,related_name="aval")
    fiador_obligado = models.CharField(max_length=35, null=True, blank=True)
   
    #  Datos Del Fiador Solidario flata agregar el empreo y antiguedad
    n_fiador=models.CharField(max_length=100, null=True, blank=True)
    a_fiador=models.CharField(max_length=100, null=True, blank=True)
    a2_fiador=models.CharField(max_length=100, null=True, blank=True)
    rfc_fiador=models.CharField(max_length=100, null=True, blank=True)
    p_fiador=models.CharField(max_length=100, null=True, blank=True)
    estado_civil_fiador=models.CharField(max_length=100, null=True, blank=True)
    nacionalidad=models.CharField(max_length=100, null=True, blank=True, default="Mexicana") 
    
    # Datos Domiciliarios del Fiador solidario
    calle_fiador=models.CharField(max_length=100, null=True, blank=True)
    municipio_fiador=models.CharField(max_length=100, null=True, blank=True)
    colonia_fiador=models.CharField(max_length=100,null=True, blank=True)
    estado_fiador=models.CharField(max_length=100, null=True, blank=True)
    n_ext_fiador=models.CharField(max_length=100,null=True, blank=True)
    n_int_fiador=models.CharField(max_length=100,null=True, blank=True, default=0)
    cp_fiador=models.BigIntegerField(null=True, blank=True)
    tel_fiador=models.BigIntegerField(null=True, blank=True)
    tel2_fiador=models.BigIntegerField(null=True, blank=True)
    email_fiador=models.EmailField(null=True, blank=True)
    
    prof_fiador=models.CharField(max_length=100, null=True, blank=True)
    empresa_fiador=models.CharField(max_length=100, null=True, blank=True)
    tel_em_fiador=models.BigIntegerField(null=True, blank=True)
    ingreso_men_fiador=models.BigIntegerField(null=True, blank=True)
    
     # recibos
    recibos=models.CharField(max_length=2, null=True, blank=True)
    
    # Datos de sus escrituras fiador solidario
    escritura_publica=models.CharField(max_length=100, null=True, blank=True)
    fecha_propiedad=models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    numero_notario=models.BigIntegerField(null=True, blank=True)
    nombre_notario=models.CharField(max_length=100, null=True, blank=True)
    
    # Datos Domiciliarios de las escrituras del Fiador solidario
    calle_escrituras=models.CharField(max_length=100, null=True, blank=True)
    num_ext_escrituras=models.CharField(max_length=100,null=True, blank=True)
    num_int_escrituras=models.CharField(max_length=100,null=True, blank=True, default=0)
    colonia_escrituras=models.CharField(max_length=100,null=True, blank=True)
    cp_escrituras=models.BigIntegerField(null=True, blank=True)    
    municipio_escrituras=models.CharField(max_length=100, null=True, blank=True)
    estado_escrituras=models.CharField(max_length=100, null=True, blank=True)
    
    # OBLIGADO PERSONA MORAL
    # Datos empresa del obligado PM
    nombre_comercial=models.CharField(max_length=100, null=True, blank=True)
    rfc_fiador_em=models.CharField(max_length=100, null=True, blank=True)
    ingreso_fiador_opm=models.BigIntegerField(null=True, blank=True)
    antiguedad_opm=models.BigIntegerField(null=True, blank=True)
    tel_opm=models.BigIntegerField(null=True, blank=True)
    cel_opm=models.BigIntegerField(null=True, blank=True)
    email_em_opm=models.EmailField(null=True, blank=True)
    pagina_web_f=models.CharField(max_length=100, null=True, blank=True)
    
    # acta constituida
    escritura_publica_ac = models.CharField(max_length=50, null=True, blank=True)
    fecha_propiedad_ac = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    nombre_notario_ac = models.CharField(max_length=50, null=True, blank=True)
    coe = models.CharField(max_length=100, null=True, blank=True)
    folio_mercantil = models.BigIntegerField(null=True, blank=True)
    
    # Direccion fiscal empresa Fiador solidario PM
    calle_em_pm=models.CharField(max_length=100, null=True, blank=True)
    n_ext_em_pm=models.CharField(max_length=100,null=True, blank=True)
    n_int_em_pm=models.CharField(max_length=100,null=True, blank=True, default=0)
    colonia_em_pm=models.CharField(max_length=100,null=True, blank=True)
    cp_em_pm=models.BigIntegerField(null=True, blank=True)
    municipio_em_pm=models.CharField(max_length=100, null=True, blank=True)
    estado_em_pm=models.CharField(max_length=100, null=True, blank=True)
    
    # Datos Generales representante legal
    nombre_rl=models.CharField(max_length=100, null=True, blank=True)
    apellido_rl=models.CharField(max_length=100, null=True, blank=True)
    apellido1_rl=models.CharField(max_length=100, null=True, blank=True)
    cel_rl=models.BigIntegerField(null=True, blank=True)
    email_rl=models.EmailField(null=True, blank=True)
    pagina_rl=models.CharField(max_length=100, null=True, blank=True)
    
    # Direccion representante legal Fiador solidario PM
    calle_rl=models.CharField(max_length=50, null=True, blank=True)
    n_ext_rl=models.CharField(max_length=100,null=True, blank=True)
    n_int_rl=models.CharField(max_length=100,null=True, blank=True, default=0)
    colonia_rl=models.CharField(max_length=100,null=True, blank=True)
    cp_rl=models.BigIntegerField(null=True, blank=True)
    municipio_rl=models.CharField(max_length=100, null=True, blank=True)
    estado_rl=models.CharField(max_length=100, null=True, blank=True)
    
     # referencia1
    nombre_empresa=models.CharField(max_length=100, null=True, blank=True)
    nombre_contacto=models.CharField(max_length=100,null=True, blank=True)
    tiempo_relacion=models.CharField(max_length=100,null=True, blank=True)
    tel_ref=models.BigIntegerField(null=True, blank=True)
    email_ref=models.EmailField(null=True, blank=True)
    cel_ref=models.BigIntegerField(null=True, blank=True)
    relacion_comercial = models.CharField(max_length=50, null=True, blank=True)
    
    # referencia2
    nombre_empresa2=models.CharField(max_length=100, null=True, blank=True)
    nombre_contacto2=models.CharField(max_length=100,null=True, blank=True)
    tiempo_relacion2=models.CharField(max_length=100,null=True, blank=True)
    tel_ref2=models.BigIntegerField(null=True, blank=True)
    email_ref2=models.EmailField(null=True, blank=True)
    cel_ref2=models.BigIntegerField(null=True, blank=True)
    relacion_comercial2 = models.CharField(max_length=50, null=True, blank=True)
        
    created=models.DateField(auto_now_add=True, null=True, blank=True)
    updated=models.DateField(auto_now_add=True, null=True, blank=True)

    # Slug 
    slug = models.SlugField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            if self.fiador_obligado == 'Obligado Solidario Persona Moral':
                slu = self.nombre_comercial +  self.rfc_fiador_em if Fiador_obligado.objects.filter(n_fiador=self.n_fiador).exists() else self.nombre_comercial
            else:
                slu = self.n_fiador + self.a_fiador+ self.rfc_fiador if Fiador_obligado.objects.filter(n_fiador=self.n_fiador).exists() else self.n_fiador + self.a_fiador
            self.slug = slugify(slu)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
         if self.fiador_obligado == 'Obligado Solidario Persona Moral':
            return f'{self.nombre_comercial}'
         else:    
            return f'{self.n_fiador} {self.a_fiador} {self.a2_fiador}'
    class Meta:
        db_table = 'fiador_obligado'

class Zip_code(models.Model):
    id = models.AutoField(primary_key=True)
    d_codigo = models.CharField(max_length=100, null=True,blank=True)
    d_asenta = models.CharField(max_length=100, null=True,blank=True)
    d_tipo_asenta = models.CharField(max_length=100, null=True,blank=True)
    d_mnpio = models.CharField(max_length=100, null=True,blank=True)
    d_estado = models.CharField(max_length=100, null=True,blank=True)
    d_ciudad = models.CharField(max_length=100, null=True,blank=True)
    
    class Meta:
        db_table = 'zip_codes'

class Arrendador(models.Model):    
    # datos personales
    id = models.AutoField(auto_created = True, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    
    regimen_fiscal=models.CharField(max_length=250, null = True, blank = True)
    # persona fisica 
    nombre_completo=models.CharField(max_length=100, blank=True)
    nacionalidad=models.CharField(max_length=100, null=True, blank=True, default="Mexicana")
    rfc=models.CharField(max_length=13, null=True, blank=True)
    identificacion=models.CharField(max_length = 100, null = True, blank = True)
    no_ide=models.CharField(max_length = 100, null = True, blank = True)
    telefono=models.CharField(max_length=100, null=True, blank=True) 
    celular=models.CharField(max_length=100, null=True, blank=True)
    estado_civil=models.CharField(max_length=100,null=True, blank=True)
    email=models.EmailField()
    
    nombre_completo_conyuge=models.CharField(max_length=100, null=True, blank=True)  
    
    # datos domiciliarios
    direccion_completa = models.CharField(max_length = 250, null = True, blank = True)
    
    # persona moral
    nombre_empresa=models.CharField(max_length = 250, null = True, blank = True)
    direccion_fiscal = models.CharField(max_length=250, null=True, blank=True)
    telefono_empresa = models.CharField(max_length=250, null=True, blank=True)
    
    escritura_publica=models.CharField(max_length=100, null=True, blank=True)
    fecha_acta = models.DateField(null=True, blank=True)
    nombre_notario=models.CharField(max_length=100, null=True, blank=True)
    numero_notario=models.BigIntegerField(null=True, blank=True)
    estado_acta = models.CharField(max_length=100, null=True, blank=True)
    folio_mercantil = models.CharField(max_length=100, null=True, blank=True)
    
    #Representante legal pm
    nombre_rl=models.CharField(max_length=100, blank=True)
    nacionalidad_rl=models.CharField(max_length=100, null=True, blank=True, default="Mexicana")
    rfc_rl=models.CharField(max_length=13, null=True, blank=True)
    identificacion_rl=models.CharField(max_length = 100, null = True, blank = True)
    no_ide_rl=models.CharField(max_length = 100, null = True, blank = True)
    celular_rl=models.CharField(max_length = 100, null = True, blank = True)
    correo_rl=models.EmailField(null=True, blank=True)
    direccion_rl=models.CharField(max_length = 250, null = True, blank = True)
    estado_civil_rl=models.CharField(max_length=100, null=True, blank=True, default="Soltero")
   
    #datos de pago
    tipo_pago = models.CharField(max_length=100, null=True, blank=True)
    banco = models.CharField(max_length=100, null=True, blank=True)
    titular = models.CharField(max_length=100, null=True, blank=True)
    no_cuenta = models.CharField(max_length=100, null=True, blank=True)
    clabe = models.CharField(max_length=100, null=True, blank=True)

    created=models.DateField(auto_now_add=True, null=True, blank=True)
    codigo_amigo = models.CharField(max_length=8, editable = False, unique=True)
    # Agregando slug
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        if self.nombre_completo:
            return f'{self.nombre_completo}'
        else:
            return f"{self.nombre_empresa}"

    def save(self, *args, **kwargs):
        characters = string.ascii_letters + string.digits
        length = 4
        print("self user",self.user)
        
        if not self.slug:
            if(self.regimen_fiscal == "Persona Fisica"):
                slu = str(self.nombre_completo).replace(" ", "_") + ''.join(random.choice(characters) for _ in range(3))
            else:
                slu = str(self.nombre_empresa).replace(" ", "_") + ''.join(random.choice(characters) for _ in range(3))   
            print(slu)
            self.slug = slugify(slu)
            name = str(self.nombre_completo[0:2])
            self.codigo_amigo = 'AR' + ''.join(random.choice(characters) for _ in range(length)) + name.upper()
            super().save(*args, **kwargs)
            
        else:
            super().save(*args, **kwargs)
      
    class Meta:
        db_table = 'arrendador'
        

class DocumentosInquilino(models.Model):
    def get_ine_upload_path(self, filename):
        inq_split = str(self.inquilino)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'inquilino/documentos/{ip}/INE/{filename}'
    
    def get_dom_upload_path(self, filename):
        inq_split = str(self.inquilino)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'inquilino/documentos/{ip}/Comprobante_de_domicilio/{filename}'
    
    def get_rfc_upload_path(self, filename):
        inq_split = str(self.inquilino)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'inquilino/documentos/{ip}/RFC/{filename}'
   
    def get_ingresos_upload_path(self, filename):
        inq_split = str(self.inquilino)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'inquilino/documentos/{ip}/Ingresos/{filename}'
   
    def get_extras_upload_path(self, filename):
        inq_split = str(self.inquilino)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'inquilino/documentos/{ip}/Documentos_extras/{filename}'
   
    def get_rl_upload_path(self, filename):
        inq_split = str(self.inquilino)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'inquilino/documentos/{ip}/Recomendacion_laboral/{filename}'
    
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    inquilino = models.ForeignKey(Inquilino, null=True, blank=True, on_delete=models.CASCADE,related_name="archivos")
    Ine = models.FileField(upload_to=get_ine_upload_path, max_length=255)
    Comp_dom = models.FileField(upload_to =get_dom_upload_path, max_length=255)
    Rfc = models.FileField(upload_to = get_rfc_upload_path, max_length=255)
    Ingresos = models.FileField(null=True, blank=True,upload_to = get_ingresos_upload_path, max_length=255)
    Extras = models.FileField(null=True, blank=True,upload_to = get_extras_upload_path, max_length=255)
    Recomendacion_laboral = models.FileField(null=True, blank=True,upload_to = get_rl_upload_path, max_length=255)
    Acta_constitutiva = models.CharField(max_length=200, null=True, blank=True)
    #comentarios
    comentarios_ine = models.CharField(max_length=200, null=True, blank=True)
    comentarios_comp = models.CharField(max_length=200, null=True, blank=True)
    comentarios_rfc = models.CharField(max_length=200, null=True, blank=True)
    comentarios_ingresos = models.CharField(max_length=200, null=True, blank=True)
    comentarios_extra = models.CharField(max_length=200, null=True, blank=True)
    comentarios_rl = models.CharField(max_length=200, null=True, blank=True)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = 'documentos_inquilino'

class DocumentosFiador(models.Model):
    def get_ine_upload_path(self, filename):
        inq_split = str(self.Fiador.inquilino)
        ip = inq_split.replace(" ", "_")
        inq_split2 = str(self.Fiador)
        ip2 = inq_split2.replace(" ", "_")
        print(ip2)
        return f'inquilino/documentos/{ip}/{ip2}/INE/{filename}'
    
    def get_dom_upload_path(self, filename):
        inq_split = str(self.Fiador.inquilino)
        ip = inq_split.replace(" ", "_")
        inq_split2 = str(self.Fiador)
        ip2 = inq_split2.replace(" ", "_")
        return f'inquilino/documentos/{ip}/{ip2}/Comprobante_de_domicilio/{filename}'
    
    def get_estado_upload_path(self, filename):
        inq_split = str(self.Fiador.inquilino)
        ip = inq_split.replace(" ", "_")
        inq_split2 = str(self.Fiador)
        ip2 = inq_split2.replace(" ", "_")
        return f'inquilino/documentos/{ip}/{ip2}/Estado_cuenta/{filename}'
    
    def get_esc_upload_path(self, filename):
        inq_split = str(self.Fiador.inquilino)
        ip = inq_split.replace(" ", "_")
        inq_split2 = str(self.Fiador)
        ip2 = inq_split2.replace(" ", "_")
        return f'inquilino/documentos/{ip}/{ip2}/Escrituras/{filename}'
    
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    Fiador = models.ForeignKey(Fiador_obligado, null=True, blank=True, on_delete=models.CASCADE,related_name="archivos")
    #Obligado y fiador
    Ine = models.FileField(upload_to=get_ine_upload_path, max_length=255)
    Comp_dom = models.FileField(upload_to =get_dom_upload_path, max_length=255)
    #obligado
    Estado_cuenta = models.FileField(null=True, blank=True,upload_to = get_estado_upload_path, max_length=255)
    #fiador
    Escrituras = models.FileField(null=True, blank=True,upload_to = get_esc_upload_path, max_length=255)
    
    #comentarios
    comentarios_ine = models.CharField(max_length=200, null=True, blank=True)
    comentarios_comp = models.CharField(max_length=200, null=True, blank=True)
    comentarios_ingresos = models.CharField(max_length=200, null=True, blank=True)
    comentarios_escrituras = models.CharField(max_length=200, null=True, blank=True)

    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = 'documentos_fiador'

class DocumentosArrendador(models.Model):
    def get_ine_upload_path(self, filename):
        inq_split = str(self.arrendador)
       
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'arrendador/{ip}/documentos/INE/{filename}'

    def get_acta_upload_path(self, filename):
        inq_split = str(self.arrendador)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'arrendador/{ip}/documentos/Acta_constitutiva/{filename}'
    
    def get_extras_upload_path(self, filename):
        inq_split = str(self.arrendador)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'arrendador/{ip}/documentos/Extras/{filename}'

    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    arrendador=models.ForeignKey(Arrendador, on_delete=models.SET_NULL, null=True, related_name='archivos')
    ine = models.FileField(upload_to=get_ine_upload_path, null=True, max_length=255)
    acta_constitutiva = models.FileField(upload_to = get_acta_upload_path, null=True, max_length=255)
    extras = models.FileField(upload_to = get_extras_upload_path, null=True, max_length=255)
    
    #comentarios
    comentarios_ine = models.CharField(max_length=200, null=True, blank=True)
    comentarios_acta_constitutiva = models.CharField(max_length=200, null=True, blank=True)
    comentarios_extras = models.CharField(max_length=200, null=True, blank=True)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    # historial_actualizacion = models.OneToOneField(HistorialActualizacionDocumentosArrendador, on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'documentos_arrendador'

class Inmuebles(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    arrendador = models.ForeignKey(Arrendador, null=True, blank=True, on_delete=models.SET_NULL)

    alias_inmueble = models.CharField(max_length=100, null=True, blank=True)
    
    estatus_inmueble = models.CharField(max_length=100, null=True, blank=True, default="Disponible")
    renta = models.BigIntegerField(null=True, blank=True)
    venta = models.BigIntegerField(null=True, blank=True)

    clave_catastral = models.CharField(max_length=100, null=True, blank=True)
    estatus_gravamen = models.CharField(max_length=100, null=True, blank=True)
    valor_catastral = models.BigIntegerField(null=True, blank=True)
    mantenimiento = models.CharField(max_length=100, null=True, blank=True)
    cuota_mantenimiento= models.BigIntegerField(null=True, blank=True)
    tipo_inmueble = models.CharField(max_length=100, null=True, blank=True)
    uso_inmueble= models.CharField(max_length=100, null=True, blank=True)
    giro=models.CharField(max_length=100, null=True, blank=True)
    op_compra = models.CharField(max_length=100, null=True, blank=True)
    municipio_alcaldia = models.CharField(max_length=100, null=True, blank=True)
    colonia = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=100, null=True, blank=True)
    estado  = models.CharField(max_length=100, null=True, blank=True)
    calle = models.CharField(max_length=100, null=True, blank=True)
    numeroExterior = models.CharField(max_length=100, null=True, blank=True)
    numeroInterior = models.CharField(max_length=100,null=True, blank=True, default=0)
    calle1 = models.CharField(max_length=100, null=True, blank=True)
    calle2 = models.CharField(max_length=100, null=True, blank=True)
    referencias = models.CharField(max_length=100, null=True, blank=True)
    n_baños = models.BigIntegerField(null=True, blank=True)
    n_medios_baños = models.BigIntegerField(null=True, blank=True)
    n_recamaras = models.BigIntegerField(null=True, blank=True)
    n_pisos = models.BigIntegerField(null=True, blank=True)
    estacionamiento_cajones = models.BigIntegerField(null=True, blank=True)
    terrenoConstruido  = models.BigIntegerField(null=True, blank=True)
    terrenoTotal = models.BigIntegerField(null=True, blank=True)    
    año_contruccion = models.BigIntegerField(null=True, blank=True)
    garage = models.CharField(max_length=100, null=True, blank=True)
    bodega = models.CharField(max_length=100, null=True, blank=True)
    terraza =  models.CharField(max_length=100, null=True, blank=True)
    alberca =  models.CharField(max_length=100, null=True, blank=True)
    cocina =  models.CharField(max_length=100, null=True, blank=True)
    amueblado = models.CharField(max_length=100, null=True, blank=True)
    cuarto_lavado =models.CharField(max_length=100, null=True, blank=True)
    mascotas = models.CharField(max_length=100, null=True, blank=True)
    gym = models.CharField(max_length=100, null=True, blank=True)
    bar = models.CharField(max_length=100, null=True, blank=True)
    restaurante_bar=models.CharField(max_length=100, null=True, blank=True)
    sala_cine = models.CharField(max_length=100, null=True, blank=True)
    salon_estudio = models.CharField(max_length=100, null=True, blank=True)
    area_comun = models.CharField(max_length=100, null=True, blank=True)
    sala_juegos = models.CharField(max_length=100, null=True, blank=True)
    salon_eventos = models.CharField(max_length=100, null=True, blank=True)
    espacio_deportivo = models.CharField(max_length=100, null=True, blank=True)
    busisness_center = models.CharField(max_length=100, null=True, blank=True)
    roof_garden = models.CharField(max_length=100, null=True, blank=True)
    otroA = models.CharField(max_length=100, null=True, blank=True)
    internet  = models.CharField(max_length=100, null=True, blank=True)
    electricidad  = models.CharField(max_length=100, null=True, blank=True)    
    agua_potable = models.CharField(max_length=100, null=True, blank=True)
    televisionCable = models.CharField(max_length=100, null=True, blank=True)
    gas = models.CharField(max_length=100, null=True, blank=True)
    lineaTelefonica = models.CharField(max_length=100, null=True, blank=True)
    drenaje = models.CharField(max_length=100, null=True, blank=True)
    seguridad = models.CharField(max_length=100, null=True, blank=True)
    camarasSeguridad  = models.CharField(max_length=100, null=True, blank=True)
    area_juegos = models.CharField(max_length=100, null=True, blank=True)
    otroS = models.CharField(max_length=100, null=True, blank=True)
    
    descripcion= models.CharField(max_length=200, null=True, blank=True)
    terminos_condiciones = models.CharField(max_length=100, null=True, blank=True)

    slug = models.SlugField(null=True, blank=True)
    created=models.DateField(auto_now_add=True, null=True, blank=True)
    updated=models.DateField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
         
        print("self user",self.user)
        print("Esta entrando a save modelo")
        characters = string.ascii_letters + string.digits
        if not self.slug:
            slu = str(self.alias_inmueble) + ''.join(random.choice(characters) for _ in range(4)) if Inmuebles.objects.filter(alias_inmueble=self.alias_inmueble).exists() else self.alias_inmueble
            self.slug = slugify(slu)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    class Meta:
        db_table = 'inmuebles'
 
class InmueblesInmobiliario(models.Model):    
    def get_dom_upload_path_inmubles_mobiliario(self, filename):
        inq_split = str(self.inmuebles.alias_inmueble)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'inmuebles/mobiliario/{ip}/Mobiliario/{filename}'

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    inmuebles = models.ForeignKey(Inmuebles, on_delete=models.CASCADE, related_name='mobiliario')
    
    observaciones = models.CharField(max_length = 200 , null=True, blank=True)
    mobiliario = models.CharField(max_length = 200 , null=True, blank=True)
    cantidad= models.BigIntegerField(default=0, null=True, blank=True)
    
    class Meta:
        db_table = 'inmuebles_mobiliario' 

   
class DocumentosInmueble(models.Model):
    def get_docs_inmueble_upload_path(self,filename):
        print("soy el self user de inmueble",self.user)
        arrendador = str(self.inmueble.arrendador.nombre_completo)
        ip = arrendador.replace(" ", "_")
        inm = str(self.inmueble.alias_inmueble)
        alias_inm = inm.replace(" ", "_")
        print(ip)
        return f'arrendador/{ip}/inmuebles/{alias_inm}/{filename}'
        #return f'{self.user}/{self.inmueble.arrendador.nombre_completo}/Inmuebles/{self.inmueble.alias_inmueble}/{filename}'
  
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    inmueble = models.ForeignKey(Inmuebles, on_delete=models.CASCADE,related_name="documentos_inmueble")
    predial = models.FileField(upload_to=get_docs_inmueble_upload_path, null=True, max_length=255)
    escrituras = models.FileField(upload_to=get_docs_inmueble_upload_path, null=True, max_length=255)
    reglamento_interno = models.FileField(upload_to=get_docs_inmueble_upload_path, null=True, max_length=255)
        
    class Meta:
        db_table = 'documentos_inmueble'

class Investigacion(models.Model):
     id = models.AutoField(primary_key=True)
     inquilino = models.ForeignKey(Inquilino, null=True, blank=True, on_delete=models.CASCADE,related_name="inv_inquilino")
     status = models.CharField(max_length=100, null=True, blank=True, default="En espera")
     identificacion = models.CharField(max_length=100, null=True, blank=True) 
     autorizacion = models.CharField(max_length=50, null=True, blank=True)
     solicitud = models.CharField(max_length=50, null=True, blank=True)
     estado_cuenta = models.CharField(max_length=50, null=True, blank=True)
     ingresos = models.CharField(max_length=50, null=True, blank=True)
     carta_laboral = models.CharField(max_length=50, null=True, blank=True)
     comentarios = models.CharField(max_length=50, null=True, blank=True)

     class Meta:
         db_table = 'investigacion'

class Agentify (models.Model):
    id = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=50, null=True, blank=True)
    apellido_materno = models.CharField(max_length=100, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100, null=True, blank=True)
    correo = models.CharField(max_length=100, null=True, blank=True)
    empresa_labora = models.CharField(max_length=100, null=True, blank=True, default='Arrendify')
    numero_celular = models.CharField(max_length=100, null=True, blank=True)
    puesto = models.CharField(max_length=100, null=True, blank=True)
    esquema_comisiones = models.CharField(max_length=100, null=True, blank=True)
    ventas = models.CharField(max_length=100, null=True, blank=True) #Tabla ventas detallado (Por hacer)

    class Meta:
        db_table = 'agentify' 

class Cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    inmueble = models.ForeignKey(Inmuebles, null=True, blank=True, on_delete=models.CASCADE, related_name="datos_inmueble")
    arrendador =  models.ForeignKey(Arrendador,null=True, blank=True, on_delete=models.CASCADE,  related_name='datos_arrendador')
    inquilino = models.ForeignKey(Inquilino, null=True, blank=True, on_delete=models.CASCADE,related_name="cot_inquilino")
    agentify = models.ForeignKey(Agentify,null=True, blank=True, on_delete=models.CASCADE, related_name='agentify') # Por hacer a llave foranea
    nombre_cotizacion = models.CharField(max_length=100, null=True, blank=True) # Agregar identificador en Frontend tipo_poliza + fecha + iniciales ARRENDADOR
    cliente = models.CharField(max_length=60, null=True, blank=True) 
    renta = models.CharField(max_length=60, null=True, blank=True)
    monto = models.CharField(max_length=100, null=True, blank=True) 
    impuesto = models.CharField(max_length=50, null=True, blank=True)
    monto_impuesto = models.CharField(max_length=100, null=True, blank=True,default = 16)
    monto_total = models.CharField(max_length=50, null=True, blank=True)
    tipo_poliza = models.CharField(max_length=50, null=True, blank=True)
    costos_extra = models.CharField(max_length=50, null=True, blank=True)
    fecha_cotizacion = models.DateField(auto_now_add=True)
    fecha_vigencia = models.DateField(null=True) # Un mes mas del auto_now
    años_cobertura = models.BigIntegerField(null=True, blank=True, default=1) 
    renta_segura = models.BigIntegerField(null=True, blank=True,default=0) 
    seguro_rc = models.BigIntegerField(null=True, blank=True,default=0) 

    #observaciones = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'cotizaciones'

@receiver(post_save, sender=Cotizacion)
def actualizar_fecha_vigencia(sender, instance, **kwargs):
    if not instance.fecha_vigencia and instance.fecha_cotizacion:
        instance.fecha_vigencia = instance.fecha_cotizacion + relativedelta(months=1)
        instance.save()
        
# envia documento generado a amazon
class Cotizacion_gen(models.Model):
    def get_dom_upload_path_documentos(self, filename):
        inq_split = str(self.cotizacion_archivo.nombre_cotizacion)
        cliente = str(self.cotizacion_archivo.cliente)
        ip = inq_split.replace(" ", "_")
        cli = cliente.replace(" ", "_")
        print(ip)
        return f'cotizacion/{cli}/{ip}/{filename}'

    id = models.AutoField(primary_key=True)
    cotizacion_archivo = models.ForeignKey(Cotizacion, on_delete=models.CASCADE, null=True, blank=True, related_name='cotizacion')
    documento_cotizacion = models.FileField(upload_to=get_dom_upload_path_documentos, max_length=255)
    fecha_vigencia = models.DateField(null=True)
    # objects = ArchivoCotizacionManager()

    class Meta:
        db_table = 'cotizacion_gen'
        
class Accion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    contador = models.IntegerField(null=True, blank=True, default = 3)
    
    class Meta:
        db_table = 'acciones_usuario'

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    nombre_problema = models.CharField(max_length=100, null=True, blank=True)
    descripcion_problema = models.CharField(max_length=100, null=True, blank=True)
    detalles_extras = models.TextField(blank=True, null=True)  # Campo para los detalles
    realizado = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'comentario'

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    # contrato = models.ForeignKey(ContratoArrendamiento, on_delete=models.CASCADE, related_name='ventas')
    agente = models.ForeignKey(Agentify, on_delete=models.CASCADE, related_name='ventas_realizadas') 
    bono_total = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.FloatField(null=True ,blank=True) 
    fecha_venta = models.DateTimeField(auto_now_add=True)
    # Otros campos relacionados con la venta
    
    def __str__(self):
        return f"Venta {self.id} - Contrato: {self.contrato.id}"
    
    class Meta:
        db_table = 'venta'
        
class Friends(models.Model):
    id = models.AutoField(primary_key=True)
    receiver = models.ForeignKey(Arrendador, related_name='amigo_arrendador', on_delete=models.CASCADE)
    sender = models.ForeignKey(Inquilino, related_name='amigo_inquilino', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'friends'

class Paquetes(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    codigo_paquete = models.CharField(max_length=100, null=True, blank=True)
    cotizacion = models.ForeignKey(Cotizacion, null = True, blank = True, on_delete=models.CASCADE, related_name='paq_cotizacion')
    arrendador =  models.ForeignKey(Arrendador,null=True, blank=True, on_delete=models.CASCADE,  related_name='paq_arrendador')
    arrendatario = models.ForeignKey(Inquilino, null=True, blank=True, on_delete=models.CASCADE,related_name="paq_inquilino")
    inmueble = models.ForeignKey(Inmuebles, null=True, blank=True, on_delete=models.CASCADE,related_name="paq_inmueble")
    fiador = models.ForeignKey(Fiador_obligado, null=True, blank=True, on_delete=models.CASCADE,related_name="paq_fiador")
    descripcion_paquete = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    datos_arrendamiento  =  models.JSONField(null=True)  
    ides  =  models.JSONField(null=True)
    firmas  =  models.JSONField(null=True)
    plazos  =  models.JSONField(null=True)

    class Meta:
        db_table = 'paquetes'

class Encuesta(models.Model):
    id = models.AutoField(primary_key=True)
    pregunta1 = models.CharField(max_length=100, null=True, blank=True)
    pregunta2 = models.CharField(max_length=100, null=True, blank=True)
    pregunta3 = models.CharField(max_length=100, null=True, blank=True)
    pregunta4 = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        db_table = 'encuesta'

class Inventario_foto(models.Model):
    def get_inv_upload_path(self, filename):
        inq_split = str(self.paquete_asociado)
        print("direccion a guardar",inq_split.__dict__)
        print(inq_split.codigo_paquete)
        print(inq_split["codigo_paquete"])
        #ip = inq_split.replace(" ", "_")
        #print(ip)
        return f'Contrato/documentos/{inq_split}/inventario_fotografico/{filename}'
    
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    paquete_asociado = models.ForeignKey(Paquetes, null=True, blank=True, on_delete=models.CASCADE,related_name="paq_asociado")
    inv_fotografico = models.FileField(upload_to=get_inv_upload_path, max_length=255)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = 'inventario_fotografico'

#FRATERNA
class Residentes(models.Model):
    # datos personales de arrendatario
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    nombre_arrendatario=models.CharField(max_length=100, blank=True)
    nacionalidad_arrendatario=models.CharField(max_length=100, null=True, blank=True, default="Mexicana")
    rfc_arrendatario=models.CharField(max_length=13, null=True, blank=True)
    identificacion_arrendatario=models.CharField(max_length = 100, null = True, blank = True)
    no_ide_arrendatario=models.CharField(max_length = 100, null = True, blank = True)
    sexo_arrendatario=models.CharField(max_length = 100, null = True, blank = True)
    celular_arrendatario=models.CharField(max_length = 100, null = True, blank = True)
    correo_arrendatario=models.EmailField(null=True, blank=True)
    empleo=models.CharField(max_length = 100, null = True, blank = True)
    domicilio_empleo=models.CharField(max_length = 100, null = True, blank = True)
    direccion_arrendatario=models.CharField(max_length = 250, null = True, blank = True)
    curp=models.CharField(max_length=100, null=True, blank=True)
    estado_civil=models.CharField(max_length=100, null=True, blank=True, default="Soltero")
    
    # datos de residente
    nombre_residente=models.CharField(max_length=100, blank=True)
    nacionalidad_residente=models.CharField(max_length=100, null=True, blank=True, default="Mexicana")
    identificacion_residente=models.CharField(max_length = 100, null = True, blank = True)
    no_ide_residente=models.CharField(max_length = 100, null = True, blank = True)
    sexo=models.CharField(max_length = 100, null = True, blank = True)
    fecha_nacimiento=models.DateField(auto_now_add=True, null=True, blank=True)
    edad=models.CharField(max_length = 100, null = True, blank = True)
    celular_residente=models.CharField(max_length = 100, null = True, blank = True)
    correo_residente=models.EmailField(null=True, blank=True)
    direccion_residente=models.CharField(max_length = 250, null = True, blank = True)
    aval=models.CharField(max_length = 100, null = True, blank = True)
    
    # ciudad_origen=models.CharField(max_length = 100, null = True, blank = True)
    # escuela_origen=models.CharField(max_length = 100, null = True, blank = True)
    # carrera=models.CharField(max_length = 100, null = True, blank = True)
    # semestre=models.CharField(max_length = 100, null = True, blank = True)
    
    # #Info personal
    # fumas=models.CharField(max_length=100, null=True, blank=True)
    # tomas=models.CharField(max_length=100, null=True, blank=True)
    # aseo=models.CharField(max_length=100, null=True, blank=True)
    # musica=models.CharField(max_length=100, null=True, blank=True)
    # tipo_musica=models.CharField(max_length=100, null=True, blank=True)
    # pasatiempos=models.CharField(max_length=255, null=True, blank=True)
    
    # Referencias Personales
    n_ref1=models.CharField(max_length=100, null=True, blank=True)
    p_ref1=models.CharField(max_length=100, null=True, blank=True)
    tel_ref1=models.BigIntegerField(null=True, blank=True)
    n_ref2=models.CharField(max_length=100, null=True, blank=True)
    p_ref2=models.CharField(max_length=100, null=True, blank=True)
    tel_ref2=models.BigIntegerField(null=True, blank=True)
    n_ref3=models.CharField(max_length=100, null=True, blank=True)
    p_ref3=models.CharField(max_length=100, null=True, blank=True)
    tel_ref3=models.BigIntegerField(null=True, blank=True)
    
    # #info de emergencia
    # nombre_emergencia=models.CharField(max_length=100, null=True, blank=True)
    # parentesco_emergencia=models.CharField(max_length=100, null=True, blank=True)
    # telefono_emergencia=models.CharField(max_length=100, null=True, blank=True)
    # celular_emergencia=models.CharField(max_length=100, null=True, blank=True)
    # correo_emergencia=models.EmailField(null=True, blank=True)
    
    class Meta:
        db_table = 'residentes'
    
class DocumentosResidentes(models.Model):
    def get_ine_upload_path(self, filename):
        inq_split = str(self.residente.nombre_residente)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Fraterna/residente/{ip}/INE/{filename}'
    
    def get_dom_upload_path(self, filename):
        inq_split = str(self.residente.nombre_residente)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Fraterna/residente/{ip}/Comprobante_de_domicilio/{filename}'
    
    def get_rfc_upload_path(self, filename):
        inq_split = str(self.residente.nombre_residente)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Fraterna/residente/{ip}/RFC/{filename}'
   
    def get_ingresos_upload_path(self, filename):
        inq_split = str(self.residente.nombre_residente)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Fraterna/residente/{ip}/Ingresos/{filename}'
   
    def get_extras_upload_path(self, filename):
        inq_split = str(self.residente.nombre_residente)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Fraterna/residente/{ip}/Documentos_extras/{filename}'
   
    def get_rl_upload_path(self, filename):
        inq_split = str(self.residente.nombre_residente)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Fraterna/residente/{ip}/Recomendacion_laboral/{filename}'
    
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    residente = models.ForeignKey(Residentes, null=True, blank=True, on_delete=models.CASCADE,related_name="archivos")
    Ine = models.FileField(upload_to=get_ine_upload_path, max_length=255)
    Ine_arr = models.FileField(null=True, blank=True, upload_to=get_ine_upload_path, max_length=255)
    Comp_dom = models.FileField(upload_to =get_dom_upload_path, max_length=255)
    Rfc = models.FileField(upload_to = get_rfc_upload_path, max_length=255)
    Ingresos = models.FileField(null=True, blank=True,upload_to = get_ingresos_upload_path, max_length=255)
    Extras = models.FileField(null=True, blank=True,upload_to = get_extras_upload_path, max_length=255)
    Recomendacion_laboral = models.FileField(null=True, blank=True,upload_to = get_rl_upload_path, max_length=255)
    Acta_constitutiva = models.CharField(max_length=200, null=True, blank=True)
    #comentarios
    comentarios_ine = models.CharField(max_length=200, null=True, blank=True)
    comentarios_comp = models.CharField(max_length=200, null=True, blank=True)
    comentarios_rfc = models.CharField(max_length=200, null=True, blank=True)
    comentarios_ingresos = models.CharField(max_length=200, null=True, blank=True)
    comentarios_extra = models.CharField(max_length=200, null=True, blank=True)
    comentarios_rl = models.CharField(max_length=200, null=True, blank=True)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = 'documentos_residentes'
        
        
#Datos De contrato
class FraternaContratos(models.Model):
    def get_plano_upload_path(self, filename):
            return f'Fraterna/plano_localizacion/{filename}'
     
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    residente = models.ForeignKey(Residentes, null=True, blank=True, on_delete=models.CASCADE, related_name="residente_contrato")
    no_depa=models.CharField(max_length = 100, null = True, blank = True)
    cama=models.CharField(max_length = 100, null = True, blank = True)
    piso=models.CharField(max_length = 100, null = True, blank = True)
    habitantes=models.CharField(max_length=100,null=True, blank=True)
    tipologia=models.CharField(max_length = 100, null = True, blank = True)
    medidas=models.CharField(max_length = 100, null = True, blank = True)
    renta=models.CharField(max_length = 100, null = True, blank = True)
    estacionamiento=models.CharField(max_length = 100, null = True, blank = True)
    #mascotas=models.CharField(max_length = 100, null = True, blank = True)
    #cajones=models.CharField(max_length = 100, null = True, blank = True)
    
    duracion=models.CharField(max_length = 100, null = True, blank = True)
    fecha_celebracion = models.DateField(null=True, blank=True)
    fecha_vigencia=models.DateField(null=True, blank=True)
    fecha_move_in=models.DateField(null=True, blank=True)
    fecha_move_out=models.DateField(null=True, blank=True)

    plano_localizacion = models.FileField(null=True, blank=True, upload_to=get_plano_upload_path, max_length=255)
    
    class Meta:
            db_table = 'fraterna_contrato'
    
    
class ProcesoContrato(models.Model):
       
        usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
        contrato = models.ForeignKey(FraternaContratos, null=True, blank=True, on_delete=models.CASCADE,related_name="contrato")
        fecha = models.DateField(null=True, blank=True)
        status_proceso=models.CharField(max_length = 100, null = True, blank = True)
        contador = models.IntegerField(null=True, blank=True, default = 2)
        
        class Meta:
            db_table = 'fraterna_proceso'
    

#FRATERNA SEMILLERO PURISIMA
class Arrendatarios_semillero(models.Model):
    # datos personales de arrendatario
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    
    #datos arrendatario y representante legal
    regimen_arrendatario=models.CharField(max_length = 250, null = True, blank = True)
    nombre_arrendatario=models.CharField(max_length=100, blank=True)
    nacionalidad_arrendatario=models.CharField(max_length=100, null=True, blank=True, default="Mexicana")
    rfc_arrendatario=models.CharField(max_length=13, null=True, blank=True)
    identificacion_arrendatario=models.CharField(max_length = 100, null = True, blank = True)
    no_ide_arrendatario=models.CharField(max_length = 100, null = True, blank = True)
    sexo_arrendatario=models.CharField(max_length = 100, null = True, blank = True)
    celular_arrendatario=models.CharField(max_length = 100, null = True, blank = True)
    correo_arrendatario=models.EmailField(null=True, blank=True)
    empleo=models.CharField(max_length = 100, null = True, blank = True)
    domicilio_empleo=models.CharField(max_length = 250, null = True, blank = True)
    direccion_arrendatario=models.CharField(max_length = 250, null = True, blank = True)
    curp=models.CharField(max_length=100, null=True, blank=True)
    estado_civil=models.CharField(max_length=100, null=True, blank=True, default="Soltero")
    
    # arrendatario persona moral
    arr_nombre_empresa=models.CharField(max_length = 250, null = True, blank = True)
    arr_telefono_empresa=models.CharField(max_length = 250, null = True, blank = True)
    arr_direccion_fiscal = models.CharField(max_length=250, null=True, blank=True)
    arr_escritura_publica=models.CharField(max_length=100, null=True, blank=True)
    arr_fecha_acta = models.DateField(null=True, blank=True)
    arr_nombre_notario=models.CharField(max_length=100, null=True, blank=True)
    arr_numero_notario=models.BigIntegerField(null=True, blank=True)
    arr_estado_acta = models.CharField(max_length=100, null=True, blank=True)
    arr_folio_mercantil = models.CharField(max_length=100, null=True, blank=True)
    
    # datos de obligado
    aval=models.CharField(max_length = 100, null = True, blank = True)
    regimen_obligado=models.CharField(max_length = 250, null = True, blank = True)
    
    nombre_obligado=models.CharField(max_length=100, blank=True)
    nacionalidad_obligado=models.CharField(max_length=100, null=True, blank=True, default="Mexicana")
    identificacion_obligado=models.CharField(max_length = 100, null = True, blank = True)
    no_ide_obligado=models.CharField(max_length = 100, null = True, blank = True)
  
    celular_obligado=models.CharField(max_length = 100, null = True, blank = True)
    correo_obligado=models.EmailField(null=True, blank=True)
    direccion_obligado=models.CharField(max_length = 250, null = True, blank = True)
    
    # obligado persona moral
    obligado_nombre_empresa=models.CharField(max_length = 250, null = True, blank = True)
    obligado_direccion_fiscal = models.CharField(max_length=250, null=True, blank=True)
    obligado_escritura_publica=models.CharField(max_length=100, null=True, blank=True)
    obligado_fecha_acta = models.DateField(null=True, blank=True)
    obligado_nombre_notario=models.CharField(max_length=100, null=True, blank=True)
    obligado_numero_notario=models.BigIntegerField(null=True, blank=True)
    obligado_estado_acta = models.CharField(max_length=100, null=True, blank=True)
    obligado_folio_mercantil = models.CharField(max_length=100, null=True, blank=True)
    
    
    #Representante legal obligado pm
    obligado_nombre_rl=models.CharField(max_length=100, blank=True)
    obligado_nacionalidad_rl=models.CharField(max_length=100, null=True, blank=True, default="Mexicana")
    obligado_curp_rl=models.CharField(max_length=100, null=True, blank=True)
    obligado_rfc_rl=models.CharField(max_length=13, null=True, blank=True)
    obligado_identificacion_rl=models.CharField(max_length = 100, null = True, blank = True)
    obligado_no_ide_rl=models.CharField(max_length = 100, null = True, blank = True)
    obligado_sexo_rl=models.CharField(max_length = 100, null = True, blank = True)
    obligado_celular_rl=models.CharField(max_length = 100, null = True, blank = True)
    obligado_correo_rl=models.EmailField(null=True, blank=True)
    
    obligado_direccion_rl=models.CharField(max_length = 250, null = True, blank = True)
    obligado_estado_civil_rl=models.CharField(max_length=100, null=True, blank=True, default="Soltero")
    
    # Referencias Personales
    n_ref1=models.CharField(max_length=100, null=True, blank=True)
    p_ref1=models.CharField(max_length=100, null=True, blank=True)
    tel_ref1=models.BigIntegerField(null=True, blank=True)
    n_ref2=models.CharField(max_length=100, null=True, blank=True)
    p_ref2=models.CharField(max_length=100, null=True, blank=True)
    tel_ref2=models.BigIntegerField(null=True, blank=True)
    n_ref3=models.CharField(max_length=100, null=True, blank=True)
    p_ref3=models.CharField(max_length=100, null=True, blank=True)
    tel_ref3=models.BigIntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'semillero_arrendatarios'
    
class DocumentosArrendatarios_semilleros(models.Model):
    def get_ine_upload_path(self, filename):
        if(self.arrendatario.nombre_arrendatario != None):
            inq_split = str(self.arrendatario.nombre_arrendatario)
        else:
            inq_split = str(self.arrendatario.arr_nombre_empresa)
        
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Semillero/arrendatario/{ip}/INE/{filename}'
    
    def get_ine_ob_upload_path(self, filename):
        if(self.arrendatario.nombre_arrendatario != None):
            inq_split = str(self.arrendatario.nombre_arrendatario)
        else:
            inq_split = str(self.arrendatario.arr_nombre_empresa)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Semillero/arrendatario/{ip}/INE/ob_{filename}'
    
    def get_dom_upload_path(self, filename):
        if(self.arrendatario.nombre_arrendatario != None):
            inq_split = str(self.arrendatario.nombre_arrendatario)
        else:
            inq_split = str(self.arrendatario.arr_nombre_empresa)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Semillero/arrendatario/{ip}/Comprobante_de_domicilio/{filename}'
    
    def get_dom_ob_upload_path(self, filename):
        if(self.arrendatario.nombre_arrendatario != None):
            inq_split = str(self.arrendatario.nombre_arrendatario)
        else:
            inq_split = str(self.arrendatario.arr_nombre_empresa)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Semillero/arrendatario/{ip}/Comprobante_de_domicilio/ob_{filename}'
    
    def get_rfc_upload_path(self, filename):
        if(self.arrendatario.nombre_arrendatario != None):
            inq_split = str(self.arrendatario.nombre_arrendatario)
        else:
            inq_split = str(self.arrendatario.arr_nombre_empresa)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Semillero/arrendatario/{ip}/RFC/{filename}'
   
    def get_ingresos_upload_path(self, filename):
        if(self.arrendatario.nombre_arrendatario != None):
            inq_split = str(self.arrendatario.nombre_arrendatario)
        else:
            inq_split = str(self.arrendatario.arr_nombre_empresa)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Semillero/arrendatario/{ip}/Ingresos/{filename}'
    
    def get_ingresos_ob_upload_path(self, filename):
        if(self.arrendatario.nombre_arrendatario != None):
            inq_split = str(self.arrendatario.nombre_arrendatario)
        else:
            inq_split = str(self.arrendatario.arr_nombre_empresa)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Semillero/arrendatario/{ip}/Ingresos/ob_{filename}'
   
    def get_extras_upload_path(self, filename):
        if(self.arrendatario.nombre_arrendatario != None):
            inq_split = str(self.arrendatario.nombre_arrendatario)
        else:
            inq_split = str(self.arrendatario.arr_nombre_empresa)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Semillero/arrendatario/{ip}/Documentos_extras/{filename}'
   
    def get_rl_upload_path(self, filename):
        if(self.arrendatario.nombre_arrendatario != None):
            inq_split = str(self.arrendatario.nombre_arrendatario)
        else:
            inq_split = str(self.arrendatario.arr_nombre_empresa)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Semillero/arrendatario/{ip}/Recomendacion_laboral/{filename}'
    
    def get_acta_upload_path(self, filename):
        if(self.arrendatario.nombre_arrendatario != None):
            inq_split = str(self.arrendatario.nombre_arrendatario)
        else:
            inq_split = str(self.arrendatario.arr_nombre_empresa)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Semillero/arrendatario/{ip}/Acta_constitutiva/{filename}'
    
    def get_acta_ob_upload_path(self, filename):
        if(self.arrendatario.nombre_arrendatario != None):
            inq_split = str(self.arrendatario.nombre_arrendatario)
        else:
            inq_split = str(self.arrendatario.arr_nombre_empresa)
        ip = inq_split.replace(" ", "_")
        print(ip)
        return f'Semillero/arrendatario/{ip}/Recomendacion_laboral/ob_{filename}'
    
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    arrendatario = models.ForeignKey(Arrendatarios_semillero, null=True, blank=True, on_delete=models.CASCADE,related_name="archivos")
    
    Ine_arrendatario = models.FileField(upload_to=get_ine_upload_path, max_length=255)
    Ine_obligado = models.FileField(null=True, blank=True, upload_to=get_ine_ob_upload_path, max_length=255)
    
    Comp_dom_arrendatario = models.FileField(upload_to =get_dom_upload_path, max_length=255)
    Comp_dom_obligado = models.FileField(null=True, blank=True, upload_to =get_dom_ob_upload_path, max_length=255)
    Rfc_arrendatario = models.FileField(upload_to = get_rfc_upload_path, max_length=255)
    
    Ingresos_arrendatario = models.FileField(null=True, blank=True,upload_to = get_ingresos_upload_path, max_length=255)
    Ingresos2_arrendatario = models.FileField(null=True, blank=True,upload_to = get_ingresos_upload_path, max_length=255)
    Ingresos3_arrendatario = models.FileField(null=True, blank=True,upload_to = get_ingresos_upload_path, max_length=255)

    Ingresos_obligado = models.FileField(null=True, blank=True,upload_to = get_ingresos_ob_upload_path, max_length=255)
    Ingresos2_obligado = models.FileField(null=True, blank=True,upload_to = get_ingresos_ob_upload_path, max_length=255)
    Ingresos3_obligado = models.FileField(null=True, blank=True,upload_to = get_ingresos_ob_upload_path, max_length=255)
    
    Acta_arrendatario = models.FileField(null=True, blank=True,upload_to = get_acta_upload_path, max_length=255)
    Acta_obligado = models.FileField(null=True, blank=True,upload_to = get_acta_ob_upload_path, max_length=255)
    
    
    Extras = models.FileField(null=True, blank=True,upload_to = get_extras_upload_path, max_length=255)
    Recomendacion_laboral = models.FileField(null=True, blank=True,upload_to = get_rl_upload_path, max_length=255)
    
    #come
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = 'documentos_arrendatarios_semilleros'
        
        
    #Datos De contrato SEMILLERO
class SemilleroContratos(models.Model):
     
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    arrendatario = models.ForeignKey(Arrendatarios_semillero, null=True, blank=True, on_delete=models.CASCADE, related_name="arrendario_contrato")
    no_depa=models.CharField(max_length = 100, null = True, blank = True)
    renta=models.CharField(max_length = 100, null = True, blank = True)
        
    duracion=models.CharField(max_length = 100, null = True, blank = True)
    
    fecha_celebracion = models.DateField(null=True, blank=True)
    fecha_terminacion=models.DateField(null=True, blank=True)

    class Meta:
            db_table = 'semillero_contrato'
    
    
class ProcesoContrato_semillero(models.Model):
       
        usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
        contrato = models.ForeignKey(SemilleroContratos, null=True, blank=True, on_delete=models.CASCADE,related_name="contrato")
        fecha = models.DateField(null=True, blank=True)
        status_proceso=models.CharField(max_length = 100, null = True, blank = True)
        contador = models.IntegerField(null=True, blank=True, default = 2)
        
        class Meta:
            db_table = 'semillero_proceso'