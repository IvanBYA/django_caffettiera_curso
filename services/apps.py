from django.apps import AppConfig


class ServicesConfig(AppConfig):
    name = 'services'
    # Nombre del modelo dentro de admin
    # 1.- Se registra aqui y en setting dentro de installed apps
    # 2.- 'services "Esto se agrega"--->   .apps.ServicesConfig', 
    verbose_name = 'Gestor de servicios'
