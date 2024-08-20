from django.db import models
from spoken_test.models.partialScores import PartialScores

# Summarize Spoken Text(SST) model 
class SummarizeSpokenText(models.Model):
    title = models.CharField(max_length=255)
    ansTimeLimit = models.IntegerField()
    audios = models.FileField(upload_to="audios/", default=None)
    ansScript = models.CharField(max_length=2500)
    scores = PartialScores()

    class Meta:
        db_table = "audio_store"

    