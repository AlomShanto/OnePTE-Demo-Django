# from django.views.generic import CreateView, UpdateView, DeleteView
# from .models.models import SummarizeSpokenText

# class SpokenTextCreateView(CreateView):
#     model = SummarizeSpokenText
#     fields = ['title', 'ansTimeLimit']
#     template_name = "C:\\Users\suhayel\Desktop\OnePTE Demo\OnePTE_Demo\spoken_test\\templates\spoken_test\spoken.html"

# class SpokenTextUpdateView(UpdateView):
#     model = SummarizeSpokenText
#     fields = ['title', 'ansTimeLimit', 'audios', 'ansScript', 'scores']
#     template_name = 'spoken_test/update_test.html'

# class SpokenTextDeleteView(DeleteView):
#     model = SummarizeSpokenText
#     template_name = 'spoken_test/delete_test.html'
#     success_url = '/'

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from spoken_test.models.models import SummarizeSpokenText
from spoken_test.forms.forms import SummarizeSpokenTextForm


@csrf_exempt
def create_spoken_text(request):
    if request.method == 'POST':
        form = SummarizeSpokenTextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spoken_test:create_test')
    else:
        form = SummarizeSpokenTextForm()
    return render(request, 'C:\\Users\suhayel\Desktop\OnePTE Demo\OnePTE_Demo\spoken_test\\templates\spoken_test\spoken.html', {'form': form})

@csrf_exempt
def update_spoken_text(request, pk):
    obj = get_object_or_404(SummarizeSpokenText, pk=pk)
    if request.method == 'POST':
        form = SummarizeSpokenTextForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('spoken_test:update_test', pk=pk)
    else:
        form = SummarizeSpokenTextForm(instance=obj)
    return render(request, 'spoken_test/update_test.html', {'form': form})

@csrf_exempt
def delete_spoken_text(request, pk):
    obj = get_object_or_404(SummarizeSpokenText, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('spoken_test:create_test')
    return render(request, 'spoken_test/delete_test.html', {'object': obj})
