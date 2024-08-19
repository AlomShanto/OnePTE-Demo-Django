from django import forms
from spoken_test.models.models import SummarizeSpokenText

class SummarizeSpokenTextForm(forms.ModelForm):
    class Meta:
        model = SummarizeSpokenText
        fields = ['title', 'ansTimeLimit']
        # If you need to customize the widget or exclude fields, you can do so here
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'ansTimeLimit': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }
