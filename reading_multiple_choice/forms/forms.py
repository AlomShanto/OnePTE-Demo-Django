from django import forms
from reading_multiple_choice.models.models import ReadingMultipleChoice

class ReadingMultipleChoiceForm(forms.ModelForm):
    class Meta:
        model = ReadingMultipleChoice
        fields = ['title', 'question','options', 'correctAns', 'ansScript']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter paragraphs separated by commas'}),
            'options': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter paragraphs separated by commas'}),
            'correctAns': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter numbers separated by commas'}),
            'ansScript': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter numbers separated by commas'}),
        }

    def clean_options(self):
        data = self.cleaned_data['options']
        return ','.join([x.strip() for x in data.split(',')])

    def clean_correctAns(self):
        data = self.cleaned_data['correctAns']
        try:
            return ','.join(map(str, [int(x.strip()) for x in data.split(',')]))
        except ValueError:
            raise forms.ValidationError("Please enter a valid list of numbers separated by commas.")

    def clean_ansScript(self):
        data = self.cleaned_data['ansScript']
        try:
            return ','.join(map(str, [int(x.strip()) for x in data.split(',')]))
        except ValueError:
            raise forms.ValidationError("Please enter a valid list of numbers separated by commas.")
