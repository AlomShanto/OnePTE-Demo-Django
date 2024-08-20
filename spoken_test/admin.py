from django.contrib import admin
from spoken_test.models.models import SummarizeSpokenText
from spoken_test.models.partialScores import PartialScores

# todo.
@admin.register(SummarizeSpokenText)
class SpokenAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'ansTimeLimit' ,
        'ansScript', 
        'scores' 
    )
