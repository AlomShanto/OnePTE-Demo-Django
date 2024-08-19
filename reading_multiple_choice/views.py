from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView

from OnePTE_Demo.reading_multiple_choice.models.models import ReadingMultipleChoice

class ReadingMultipleChoiceCreateView(CreateView):
    model = ReadingMultipleChoice()
    template_name = 'reading_multiple_choice/create_test.html'

class ReadingMultipleChoiceUpdateView(UpdateView):
    model = ReadingMultipleChoice()
    template_name = 'reading_multiple_choice/update_test.html'


class ReadingMultipleChoiceDeleteView(DeleteView):
    model = ReadingMultipleChoice()
    # template_name = 'reading_multiple_choice/delete_test.html'
