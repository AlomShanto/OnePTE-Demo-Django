from django.db import models

# Reading Multiple Choice(RMMCQ) model 

class ReadingMultipleChoice(models.Model):
    title = models.CharField(max_length=255)
    question = models.TextField(default="")
    options = models.TextField(default="")
    correctAns = models.TextField(default="")  # Store list as comma-separated string
    ansScript = models.TextField(default="")  # Store list as comma-separated string
    score = models.IntegerField(default=0)