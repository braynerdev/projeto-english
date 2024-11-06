from django.contrib import admin
from .models import  Palavras

    
@admin.register(Palavras)
class PalavrasAdmin(admin.ModelAdmin):
    list_display = ('user','palavra', 'traducao', 'criado','modificado')