from django.db import models

# Re-Ordering Paragraphs(RO) model 

class ReorderingParagraph(models.Model):
    title = models.CharField(max_length=255)
    question = models.TextField(default="")  # Store list as comma-separated string
    correctAns = models.TextField(default="")  # Store list as comma-separated string
    ansScript = models.TextField(default="")  # Store list as comma-separated string
    score = models.IntegerField(default=0)
