from django.urls import path 
from . import views

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('usuario/', views.adopta, name='usuario'),
    path('formulario/', views.formulario, name='formulario'),
    #path('usuario.html', views.register_view, name='register_view'),
    #path('formulario.html', views.dog_list, name ='adopcion'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('post/new/', views.post_new, name='post_new'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
]