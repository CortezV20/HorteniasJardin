from django.contrib import admin
from .models import Usuario, Cuenta

# Register your models here.
admin.site.register(Cuenta)
admin.site.register(Usuario)