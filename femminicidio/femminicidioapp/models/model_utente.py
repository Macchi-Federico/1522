from django.db import models

# Create your models here.
class Utente(models.Model):

    Regioni = [
        ('Abruzzo', 'Abruzzo'),
        ('Basilicata', 'Basilicata'),
        ('Calabria', 'Calabria'),
        ('Campania', 'Campania'),
        ('Emilia-Romagna', 'Emilia-Romagna'),
        ('Friuli-Venezia Giulia', 'Friuli-Venezia Giulia'),
        ('Lazio', 'Lazio'),
        ('Liguria', 'Liguria'),
        ('Lombardia', 'Lombardia'),
        ('Marche', 'Marche'),
        ('Molise', 'Molise'),
        ('Piemonte', 'Piemonte'),
        ('Puglia', 'Puglia'),
        ('Sardegna', 'Sardegna'),
        ('Sicilia', 'Sicilia'),
        ('Toscana', 'Toscana'),
        ('Trentino-Alto Adige', 'Trentino-Alto Adige'),
        ('Umbria', 'Umbria'),
        ('Valle d\'Aosta', 'Valle d\'Aosta'),
        ('Veneto', 'Veneto')
    ]

    nome = models.CharField(max_length=20, null=True, blank=True,)
    cognome = models.CharField(max_length=20, null=True, blank=True,)
    cell_email = models.CharField(max_length=20, null=False, blank=False,unique=True )
    regione = models.CharField(max_length=100, choices=Regioni, null=True, blank=True)



    def __str__(self):
        return f"{self.nome} {self.cognome} {self.cell_email} {self.regione}"

    
    