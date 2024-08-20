from django.contrib import admin
from reorder_paragraph.models.models import ReorderingParagraph

# Register your models here.
@admin.register(ReorderingParagraph)
class ReorderingParagraphs(admin.ModelAdmin):
    list_display = ('title', 'question', 'ansScript','correctAns', 'score')
