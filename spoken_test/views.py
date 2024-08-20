from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from spoken_test.models.models import SummarizeSpokenText
from spoken_test.forms.forms import SummarizeSpokenTextForm

@csrf_exempt
def create_spoken_text(request):
    if request.method == 'POST':
        form = SummarizeSpokenTextForm(request.POST, request.FILES)  # Use request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'SummarizeSpokenText created successfully'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def all_details_spoken_text(request):
    if request.method == 'GET':
        objs = SummarizeSpokenText.objects.all()
        data = []
        for obj in objs:
            data.append({
                'id': obj.id,
                'title': obj.title,
                'ansTimeLimit': obj.ansTimeLimit,
                'audios': obj.audios.url if obj.audios else None,  # Return the URL to the file if available
                'ansScript': obj.ansScript,
                'scores': str(obj.scores) if obj.scores else None,  # Adjust based on how PartialScores is represented
            })
        return JsonResponse({'status': 'success', 'data': data}, status=200)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def update_spoken_text(request, pk):
    obj = get_object_or_404(SummarizeSpokenText, pk=pk)
    if request.method == 'POST':
        form = SummarizeSpokenTextForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'SummarizeSpokenText updated successfully'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def delete_spoken_text(request, pk):
    obj = get_object_or_404(SummarizeSpokenText, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return JsonResponse({'status': 'success', 'message': 'SummarizeSpokenText deleted successfully'}, status=200)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
