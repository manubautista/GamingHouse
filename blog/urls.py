from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.blog, name="Blog"),
    path('categoria/<categoria_id>/', views.categoria, name="categoria")

]
