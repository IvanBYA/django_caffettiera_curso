from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample, name="sample"),
    path('<int:page_id>/', views.page, name="page"),
]