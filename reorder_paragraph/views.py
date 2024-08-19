# from django.shortcuts import render, redirect
# from django.views.generic import CreateView, UpdateView, DeleteView

# from OnePTE_Demo.reorder_paragraph.models.models import ReorderingParagraph


# class ReorderParagraphCreateView(CreateView):
#     model = ReorderingParagraph()
#     template_name = 'reorder_paragraph/create_test.html'

# class ReorderParagraphUpdateView(UpdateView):
#     model = ReorderingParagraph()
#     template_name = 'reorder_paragraph/update_test.html'


# class ReorderParagraphDeleteView(DeleteView):
#     model = ReorderingParagraph()
#     # template_name = 'reorder_paragraph/delete_test.html'

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from reorder_paragraph.models.models import ReorderingParagraph
from reorder_paragraph.forms.forms import ReorderingParagraphForm


@csrf_exempt
def create_reordering_paragraph(request):
    if request.method == 'POST':
        form = ReorderingParagraphForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reorder_paragraph:create_test')
    else:
        form = ReorderingParagraphForm()
    return render(request, 'C:\\Users\suhayel\Desktop\OnePTE Demo\OnePTE_Demo\reorder_paragraph\\templates\reorder_paragraph\reordering.html', {'form': form})

@csrf_exempt
def update_reordering_paragraph(request, pk):
    obj = get_object_or_404(ReorderingParagraph, pk=pk)
    if request.method == 'POST':
        form = ReorderingParagraphForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('reorder_paragraph:update_test', pk=pk)
    else:
        form = ReorderingParagraphForm(instance=obj)
    return render(request, 'reorder_paragraph/update_test.html', {'form': form})

@csrf_exempt
def delete_reordering_paragraph(request, pk):
    obj = get_object_or_404(ReorderingParagraph, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('reorder_paragraph:create_test')
    return render(request, 'reorder_paragraph/delete_test.html', {'object': obj})