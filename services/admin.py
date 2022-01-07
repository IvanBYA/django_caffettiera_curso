from django.contrib import admin
from .models import Service

# Register your models here.

# Configuracion para aplicar ajuste de solo vista los campos 
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Service, ServiceAdmin)