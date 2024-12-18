from django.contrib import admin
from django.urls import path, include  # Importa include
from django.shortcuts import redirect

# Función de redirección
def redirigir_a_login(request):
    return redirect('login')  # 'login' es el nombre de la URL de tu vista de login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirigir_a_login, name='root'),  # Redirige la raíz al login
    path('', include('gestion_turnos.urls')),  # Incluye las rutas de tu app
]
