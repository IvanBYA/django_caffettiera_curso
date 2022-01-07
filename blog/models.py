from django.db import models
# timezone - detecta la zona horaria donde esta configurado el proyecto
from django.utils.timezone import now
# User - Aqui contiene todos los usuarios que estan dentro del administrador de Django
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
    
    class Meta:
        verbose_name = ("categoria")
        verbose_name_plural = ("categorias")
        ordering = ["-created"]


    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    # Fecha de publicacion Manual que está podra establecerla el autor.
    published = models.DateTimeField(verbose_name="Fecha de Publicación", default=now)
    #null / blank TRUE = No vamos a obligar a que el usuario agregue una imagen
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    # El autor lo enlazaremos con una clave foranea
    
    # author = models.ForeignKey("Nombre del modelo", )
    
    # 'on_delete' = models.Cascacde - Si  un modelo está relacionado con otro modelo, en este caso el autor con el usuario, esta accion on_delete indicara a Django lo que tiene que hacer el autor al borrar las entradas que tenian este autor.  
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    # Hacemos referencia al mismo modelo de aqui arriba
    # Vamos a relacionar muchos a muchos 
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
    
    class Meta:
        verbose_name = ("entrada")
        verbose_name_plural = ("entradas")
        ordering = ["-created"]


    def __str__(self):
        return self.title
