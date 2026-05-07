from django.db import models
from .model_utente import Utente

class Testimonianza(models.Model):
    STATI = [
        ('in_attesa',  'In attesa'),
        ('accettata',  'Accettata'),
        ('rifiutata',  'Rifiutata'),
    ]

    utente = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name='testimonianze')
    testo  = models.TextField()
    data   = models.DateTimeField(auto_now_add=True)
    stato  = models.CharField(max_length=20, choices=STATI, default='in_attesa')

    def __str__(self):
        return f"Testimonianza di {self.utente.nome} del {self.data}"