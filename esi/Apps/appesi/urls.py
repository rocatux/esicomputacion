from django.conf.urls import url,include
from django.contrib import admin
from .views import IndexView,IngresarCursoView,IngresarTipoCursoView,IngresarTipoPagoView,LoginView,logoutview, CrearUsuarioView, ContactoView, QuienView

urlpatterns = [
   url(r'^$', IndexView.as_view(), name ='index'),
   url(r'^IngCurso$', IngresarCursoView.as_view(), name ='IngCurso'),
   url(r'^IngTipoCurso$', IngresarTipoCursoView.as_view(), name ='IngTipoCurso'),
   url(r'^IngTipoPago$', IngresarTipoPagoView.as_view(), name ='IngTipoPago'),
   url(r'^Login$', LoginView.as_view(), name='Login'),
   url(r'^SalirUser$', logoutview, name='logout'),
   url(r'^CrearUsuario$', CrearUsuarioView.as_view(), name='CrearUsuario'),
   url(r'^Contacto$', ContactoView.as_view(),name='contacto'),
   url(r'^Quien$', QuienView.as_view(),name='quien'),

]