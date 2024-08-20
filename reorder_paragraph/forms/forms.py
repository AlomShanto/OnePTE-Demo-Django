from django import forms
from reorder_paragraph.models.models import ReorderingParagraph

class ReorderingParagraphForm(forms.ModelForm):
    class Meta:
        model = ReorderingParagraph
        fields = ['title', 'question', 'correctAns', 'ansScript']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'question': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'correctAns': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter numbers separated by commas'}),
            'ansScript': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter numbers separated by commas'}),
        }

    def clean_question(self):
        data = self.cleaned_data['question']
        return ','.join([x.strip() for x in data.split(',')])

    def clean_correctAns(self):
        data = self.cleaned_data['correctAns']
        try:
            return ','.join(map(str, [int(x.strip()) for x in data.split(',')]))
        except ValueError:
            raise forms.ValidationError("Please enter a valid list of numbers separated by commas.")

    def clean_ansScript(self):
        data = self.cleaned_data.get('ansScript', '')  # Handle empty case
        if data:
            try:
                return ','.join(map(str, [int(x.strip()) for x in data.split(',')]))
            except ValueError:
                raise forms.ValidationError("Please enter a valid list of numbers separated by commas.")
        return data  # Return empty if no data
