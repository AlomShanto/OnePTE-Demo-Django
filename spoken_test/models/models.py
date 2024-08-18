from django.db import models
from spoken_test.models.partialScores import PartialScores

# Summarize Spoken Text(SST) model 
class SST():
    title = models.CharField()
    ansTimeLimit = models.IntegerField()
    audios = models.AutoField()
    ansScript = models.CharField()
    scores = PartialScores()
    