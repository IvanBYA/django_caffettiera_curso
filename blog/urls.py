from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    #              |Cadena de caracteres| 
    path('category/<int:category_id>/', views.category, name="category"),
]