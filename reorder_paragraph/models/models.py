from django.db import models

# Re-Ordering Paragraphs(RO) model 
class ReorderingParagraph(models.Model):
    title = models.CharField(max_length=255)
    question = list[models.IntegerField()]
    correctAns = list[models.ImageField()]
    ansScript = list[models.IntegerField()]

class Paragraph(models.Model):
    paragraphNo = models.IntegerField()
    questionScript = models.CharField(max_length=2500)