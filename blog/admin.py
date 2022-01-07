from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    # Campos de solo lectura
    readonly_fields = ('created', 'updated')
    # Desplegar solamente estas columnas en admin
    list_display = ('title', 'author','published','post_categories')
    # Ordena primero por author y despues ordena por fecha de publicación
    ordering = ('author', 'published')
    
    '''Ordenar por un elemento
    
    ordering = ('author',)   <----- Importante dejar una coma despues del campo a ordenar
    '''
    # Barra de busqueda por campo
    search_fields = ('title','content','author__username','categories__name')
    
    # Forma mas comoda de navegar en la parte superior entre fechas
    date_hierarchy = 'published'
        
    list_filter = ('author__username','categories__name')

    # El objeto hará referencia a cada fila/elemento se mostrara este objeto
    # =================== Este codigo muestra las categorias de cada POST manualmente ================#
    def post_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"
    #=================================================================================================#


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

