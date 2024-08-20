from django.contrib import admin
from reading_multiple_choice.models.models import ReadingMultipleChoice

# Register your models here.
@admin.register(ReadingMultipleChoice)
class ReadingMultipleChoices(admin.ModelAdmin) :
    list_display = ('title', 'question', 'options', 'correctAns', 'ansScript', 'score')
