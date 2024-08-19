from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView

from OnePTE_Demo.reorder_paragraph.models.models import ReorderingParagraph


class ReorderParagraphCreateView(CreateView):
    model = ReorderingParagraph()
    template_name = 'reorder_paragraph/create_test.html'

class ReorderParagraphUpdateView(UpdateView):
    model = ReorderingParagraph()
    template_name = 'reorder_paragraph/update_test.html'


class ReorderParagraphDeleteView(DeleteView):
    model = ReorderingParagraph()
    # template_name = 'reorder_paragraph/delete_test.html'
