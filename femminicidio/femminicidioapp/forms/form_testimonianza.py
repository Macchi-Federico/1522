from django import forms
from ..models.model_testimonianza import Testimonianza

class TestimonianzaForm(forms.ModelForm):
    class Meta:
        model = Testimonianza
        fields = ['testo']
        widgets = {
            'testo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Raccontaci cosa ti è successo...',
                'rows': 8
            })
        }