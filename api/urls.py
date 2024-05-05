from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'tipoDocumento', views.TipoDocViewSet)
router.register(r'institucion', views.InstitucionViewSet)
router.register(r'departamento', views.DepartamentoViewSet)
router.register(r'puesto', views.PuestoViewSet)
router.register(r'uuario', views.UsuarioViewSet)
router.register(r'documento', views.DocumentoViewSet)



urlpatterns = [
    path('', include(router.urls))
]