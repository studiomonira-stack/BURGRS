from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('menu/', views.hem, name='hem'),
    path('youmatter/', views.youmatter, name='youmatter'),
    path('nyheter/', views.nyheter, name='nyheter'),
    path('erbjudanden/', views.erbjudanden, name='erbjudanden'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('rosta/', views.rosta, name='rosta'),
    path('offers/use/<int:erbjudande_id>/', views.anvand_erbjudande, name='anvand_erbjudande'),
    path('privacy/', views.privacy, name='privacy'),
]