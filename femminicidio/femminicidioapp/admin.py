from django.contrib import admin
from .models.model_utente import Utente
from .models.model_testimonianza import Testimonianza

admin.site.register(Utente)
admin.site.register(Testimonianza)