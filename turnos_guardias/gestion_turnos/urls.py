from django.urls import path
from gestion_turnos import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('ver-usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('exportar-usuarios-excel/', views.exportar_usuarios_excel, name='exportar_usuarios_excel'),
    path('registrar-guardia/', views.registrar_guardia, name='registrar_guardia'),
    path('ver-sucursales/', views.ver_sucursales, name='ver_sucursales'),
    path('registrar-sucursal/', views.registrar_sucursal, name='registrar_sucursal'),
    path('exportar-sucursales-excel/', views.exportar_sucursales_excel, name='exportar_sucursales_excel'),
    path('logout/', views.logout_view, name='logout'),
    path('optimizar-turnos/', views.optimizar_turnos, name='optimizar_turnos'),
    path('optimizar-recursos/', views.optimizar_recursos_humanos, name='optimizar_recursos'),
    path('exportar-usuarios-asignados/<int:sucursal_id>/', views.exportar_usuarios_asignados, name='exportar_usuarios_asignados'),
    # Editar y Eliminar Sucursales
    path('editar-sucursal/<int:pk>/', views.EditarSucursalView.as_view(), name='editar_sucursal'),
    path('eliminar-sucursal/<int:pk>/', views.EliminarSucursalView.as_view(), name='eliminar_sucursal'),

    # Editar y Eliminar Guardias
    path('editar-guardia/<int:pk>/', views.EditarGuardiaView.as_view(), name='editar_guardia'),
    path('eliminar-guardia/<int:pk>/', views.EliminarGuardiaView.as_view(), name='eliminar_guardia'),

    path('calcular-guardias-cercanos/', views.calcular_guardias_cercanos, name='calcular_guardias_cercanos'),
    path('enviar-notificacion/<int:guardia_id>/<int:sucursal_id>/<int:turno>/', views.enviar_notificacion, name='enviar_notificacion'),

    path('ver-notificaciones/', views.ver_notificaciones, name='ver_notificaciones'),
    path('responder-notificacion/<int:notificacion_id>/<str:respuesta>/', views.responder_notificacion, name='responder_notificacion'),
    path('ver-asignaciones/', views.ver_asignaciones_aprobadas, name='ver_asignaciones_aprobadas'),
    path('ver_usuarios_asignados/<int:sucursal_id>/', views.ver_usuarios_asignados, name='ver_usuarios_asignados'),
    path('desasignar_usuario/<int:notificacion_id>/', views.desasignar_usuario, name='desasignar_usuario'),
    path('mis-sucursales/', views.ver_sucursales_asignadas, name='ver_sucursales_asignadas'),
]


