from django.contrib import admin
from practice_history.models.models import SubmissionHistory

@admin.register(SubmissionHistory)
class SubHist(admin.ModelAdmin) :
    list_display = ('user', 'exam_type', 'question_id', 'timestamp')
    
