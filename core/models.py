from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Atualizado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    class Meta:
        abstract = True
    

class Palavras(Base):
    user = models.ForeignKey(User, max_length=100, default=10, on_delete=models.CASCADE)
    palavra = models.CharField('Palavra', max_length=100)
    traducao = models.CharField('Tradução', max_length=100)
    class Meta:
        verbose_name = 'Palavra'
        verbose_name_plural = 'Palavras'
    def __str__(self):
        return self.palavra
    
