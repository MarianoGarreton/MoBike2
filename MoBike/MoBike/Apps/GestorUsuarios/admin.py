from django.contrib import admin
from MoBike.Apps.GestorUsuarios.models import *

# Register your models here.

admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(UsuarioTipo)
admin.site.register(Comuna)