from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from Product import views

"""
Agregamos las rutas de:
    createBasket -> Crear el carrito de compras
"""
urlpatterns = [
    path('createbasket/', views.createBasket),
    path('addproduct/', views.addProduct),
    path('sumaproduc/', views.sumProduct),

]
urlpatterns = format_suffix_patterns(urlpatterns)
