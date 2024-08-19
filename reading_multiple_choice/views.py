from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from reading_multiple_choice.models.models import ReadingMultipleChoice
from reading_multiple_choice.forms.forms import ReadingMultipleChoiceForm

# class ReadingMultipleChoiceCreateView(CreateView):
#     model = ReadingMultipleChoice()
#     template_name = 'reading_multiple_choice/create_test.html'

# class ReadingMultipleChoiceUpdateView(UpdateView):
#     model = ReadingMultipleChoice()
#     template_name = 'reading_multiple_choice/update_test.html'


# class ReadingMultipleChoiceDeleteView(DeleteView):
#     model = ReadingMultipleChoice()
#     # template_name = 'reading_multiple_choice/delete_test.html'

@csrf_exempt
def create_reading_multiple_choice(request):
    if request.method == 'POST':
        form = ReadingMultipleChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reading_multipe_choice:create_test')
    else:
        form = ReadingMultipleChoiceForm()
    return render(request, 'C:\\Users\suhayel\Desktop\OnePTE Demo\OnePTE_Demo\reading_multipe_choice\\templates\reading_multipe_choice\reordering.html', {'form': form})

@csrf_exempt
def update_reading_multiple_choice(request, pk):
    obj = get_object_or_404(ReadingMultipleChoice, pk=pk)
    if request.method == 'POST':
        form = ReadingMultipleChoiceForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('reading_multipe_choice:update_test', pk=pk)
    else:
        form = ReadingMultipleChoiceForm(instance=obj)
    return render(request, 'reading_multipe_choice/update_test.html', {'form': form})

@csrf_exempt
def delete_reading_multiple_choice(request, pk):
    obj = get_object_or_404(ReadingMultipleChoice, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('reading_multipe_choice:create_test')
    return render(request, 'reading_multipe_choice/delete_test.html', {'object': obj})