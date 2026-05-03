from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.app_list, name='app_list'),
    path('create/', views.app_create, name='app_create'),
    path('<int:app_id>/edit/', views.app_edit, name='app_edit'),
    path('<int:app_id>/delete/', views.app_delete, name='app_delete'),
]