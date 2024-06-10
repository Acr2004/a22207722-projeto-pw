from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view1),
    path('football/', views.index_view2),
    path('handball/', views.index_view3),
    path('basketball/', views.index_view4),
]