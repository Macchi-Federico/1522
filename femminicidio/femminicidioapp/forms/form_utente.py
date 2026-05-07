from django import forms
from ..models.model_utente import Utente
class UtenteForm(forms.ModelForm):
    class Meta:
        model = Utente
        fields = ['nome','cognome','cell_email','regione']

        widgets= {

            "nome": forms.TextInput(
                attrs={'class': '', 
                       'placeholder': 'nome'}
            ),

            "cognome": forms.TextInput(
                attrs={'class': '',
                       'placeholder': 'cognome'}
            ),

            "cell_email": forms.TextInput(
                attrs={'class': '',
                       'placeholder': 'email o cell' }
            ),

            "regione": forms.Select(
                attrs={'class': 'form-select',
                       'placeholder': 'regione'}    
            ),
            
        }