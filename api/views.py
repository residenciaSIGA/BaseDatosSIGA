from django.http import JsonResponse
from rest_framework import viewsets, status
from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

class TipoDocViewSet(viewsets.ModelViewSet):
    queryset = TipoDoc.objects.all()
    serializer_class = TipoDocSerializer

class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class PuestoViewSet(viewsets.ModelViewSet):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

# Agregar la vista de inicio de sesión
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        correo_electronico = request.data.get('correo_electronico')  # Utiliza 'correo_electronico' como username
        pssword = request.data.get('pssword')  # Corrige 'pssword' a 'password'

        print("Correo electrónico proporcionado:", correo_electronico)
        print("Contraseña proporcionada:", pssword)
        print(f"Tabla de la base de datos para el modelo Usuario: {Usuario._meta.db_table}")
          # Consulta a la base de datos para obtener los datos de usuarios
        usuarios = Usuario.objects.all()

        # Imprimir los datos de la tabla 'api_usuario'
        print("Datos de la tabla 'api_usuario':")
        for usuario in usuarios:
            print("idUsu:", usuario.id)
            print("nombre:", usuario.nombre)
            print("correo_electronico:", usuario.correo_electronico)
            print("contrasea:", usuario.pssword)
            print("departamento:", usuario.departamento)
            print("puesto:", usuario.puesto)

        # Buscar el usuario por correo electrónico
        try:
            usuario = Usuario.objects.get(correo_electronico=correo_electronico)
        except Usuario.DoesNotExist:
            usuario = None

        # Verificar si el usuario existe y la contraseña coincide
        if usuario is not None and usuario.pssword == pssword:
            access_token = AccessToken.for_user(usuario)
            refresh_token = RefreshToken.for_user(usuario)

              # Obtener el token JWT como cadena
            access_token_str = str(access_token)
            refresh_token_str = str(refresh_token)

            return JsonResponse({
                'refresh': refresh_token_str,
                'access': access_token_str,
            }, status=status.HTTP_200_OK)
        else:
            # Si las credenciales son incorrectas, devolver un error de autorización
            return JsonResponse({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)

