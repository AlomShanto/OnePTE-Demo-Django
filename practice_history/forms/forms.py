from django import forms
from practice_history.models.models import SubmissionHistory

class SubmissionHistoryForm(forms.ModelForm):
    class Meta:
        model = SubmissionHistory
        fields = ['user', 'exam_type', 'question_id']  # Exclude 'timestamp' as it's auto-populated
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'exam_type': forms.TextInput(attrs={'class': 'form-control'}),
            'question_id': forms.NumberInput(attrs={'class': 'form-control'}),
        }