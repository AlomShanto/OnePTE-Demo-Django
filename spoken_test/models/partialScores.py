from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class PartialScores(models.Model):
    questionId = models.IntegerField()
    contentPoints = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(2) ]
    )
    formPoints = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(2) ]
    )
    grammerPoints = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(2) ]
    )
    vocabularyPoints = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(2) ]
    )
    spellingPoints = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(2) ]
    )
