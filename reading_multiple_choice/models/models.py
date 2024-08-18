from django.db import models

# Reading Multiple Choice(RMMCQ) model 

class Option(models.Model):
    details = models.CharField(max_length=2500)

class SingleMCQ(models.Model):
    title = models.CharField(max_length=255)
    options = list[Option()]
    correctOption = models.IntegerField()

class ReadingMultipleChoice(models.Model):
    title = models.CharField(max_length=255)
    question = list[SingleMCQ()]
    ansScript = list[models.IntegerField()]
    totalScore = models.IntegerField()