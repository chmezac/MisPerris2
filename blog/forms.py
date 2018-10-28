from django import forms
from .models import Post, Adoptante
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class RegisterForm(forms.Form):
    usuario = forms.CharField(label="Nombre de Usuario (Nickname)", widget=forms.TextInput())
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput())
    apellido = forms.CharField(label="Apellido", widget=forms.TextInput())
    email = forms.CharField(label="E-mail", widget=forms.TextInput())
    password_one = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False), min_length=8)
    password_two = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(render_value=False))

    def clean_usuario(self):
        username = self.cleaned_data['usuario']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Nombre de usuario ya existente")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("E-mail ya existente")

    def clean_password_two(self):
        password_one = self.cleaned_data['password_one']
        password_two = self.cleaned_data['password_two']

        if(password_one == password_two):
            pass
        else:
            raise forms.ValidationError("Las contraseñas NO son iguales")




class AdoptanteForm(forms.ModelForm):

    class Meta:
        model = Adoptante
        fields = ('correo', 'run', 'nombreCompleto', 'telefono','region','vivienda')

    def clean_correo(self):
        correo = self.cleaned_data['correo']

        correo_base, proveedor = correo.split("@")
        dominio, extension = proveedor.split(".")
        if not dominio == "gmail":
            raise ValidationError("Aqui se registra con gmail")
        elif not extension == "com":
            raise ValidationError("Aqui se registra con gmail.com")
        return correo


    def clean_run(self):
        run = self.cleaned_data['run']
        if not "-" in run:
            raise ValidationError("Digita tu run sin puntos pero con guión")
        elif len(run) <= 8:
            raise ValidationError("Ingresa un rut con un minimo de 9 caracteres")
        return run

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono.isalpha():
            raise ValidationError('El telefono no puede contener letras')
        elif len(telefono) <= 8:
            raise ValidationError("Ingresa un telefono con un 9 digitos")
        return telefono

    def clean_nombreCompleto(self):
        nombreCompleto = self.cleaned_data['nombreCompleto']
        if len(nombreCompleto.split(' ')) < 4 :
            raise ValidationError("Por favor ingresa tu nombre completo")
        return nombreCompleto    