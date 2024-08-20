from django.db import models
from django.contrib.auth.models import User

class SubmissionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=255)  # e.g., 'ReadingMultipleChoice'
    question_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)