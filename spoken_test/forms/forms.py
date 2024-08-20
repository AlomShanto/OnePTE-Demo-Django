from django import forms
from spoken_test.models.models import SummarizeSpokenText

class SummarizeSpokenTextForm(forms.ModelForm):
    class Meta:
        model = SummarizeSpokenText
        fields = ['title', 'audios', 'ansTimeLimit']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'audios': forms.FileInput(attrs={'class': 'form-control'}),
            'ansTimeLimit': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def clean_audios(self):
        audios = self.cleaned_data.get('audios')
        if not audios:
            raise forms.ValidationError("This field is required.")
        return audios
