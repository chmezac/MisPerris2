from django.contrib import admin
from .models import Post, Dog, AdoptionRegister, Adoptante, Adoptado

admin.site.register(Post)
admin.site.register(Dog)
admin.site.register(AdoptionRegister)

admin.site.register(Adoptante)
admin.site.register(Adoptado)