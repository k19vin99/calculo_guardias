from django import forms
from django.contrib.auth.models import User, Group
from .models import Guardia, Sucursal

class GuardiaRegistroForm(forms.ModelForm):
    # Campos adicionales
    username = forms.CharField(label="Nombre de Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    grupo = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label="Grupo")

    class Meta:
        model = Guardia
        fields = ['direccion', 'latitud', 'longitud', 'disponibilidad_horas', 'activo', 'preferencia_turno']
        labels = {
            'preferencia_turno': 'Preferencia de Turno',
        }
        
    def save(self, commit=True):
        # Crear un usuario
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )

        # Asignar el usuario al grupo seleccionado
        grupo = self.cleaned_data['grupo']
        user.groups.add(grupo)

        # Crear el objeto Guardia
        guardia = super().save(commit=False)
        guardia.user = user

        if commit:
            guardia.save()
        return guardia


class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'direccion', 'latitud', 'longitud', 'requerimiento_turnos']
