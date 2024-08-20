from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from reading_multiple_choice.models.models import ReadingMultipleChoice
from reading_multiple_choice.forms.forms import ReadingMultipleChoiceForm

@csrf_exempt
def create_reading_multiple_choice(request):
    if request.method == 'POST':
        form = ReadingMultipleChoiceForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Reading Multiple Choice created successfully',
                'id': obj.pk
            }, status=201)
        else:
            return JsonResponse({
                'status': 'error',
                'errors': form.errors
            }, status=400)
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=405)

@csrf_exempt
def all_details_reading_multiple_choice(request):
    if request.method == 'GET':
        objs = ReadingMultipleChoice.objects.all()
        data = []
        for obj in objs:
            data.append({
                'id': obj.id,
                'title': obj.title,
                'question': obj.question.split(','),  # Convert comma-separated string back to list
                'options': obj.options.split(','),  # Convert comma-separated string back to list
                'correctAns': list(map(int, obj.correctAns.split(','))),  # Convert comma-separated string to list of integers
                'ansScript': list(map(int, obj.ansScript.split(','))) if obj.ansScript else [],  # Convert if not empty
                'score': obj.score,
            })
        return JsonResponse({'status': 'success', 'data': data}, status=200)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def update_reading_multiple_choice(request, pk):
    obj = get_object_or_404(ReadingMultipleChoice, pk=pk)
    if request.method == 'POST':
        form = ReadingMultipleChoiceForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Reading Multiple Choice updated successfully'
            }, status=200)
        else:
            return JsonResponse({
                'status': 'error',
                'errors': form.errors
            }, status=400)
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=405)

@csrf_exempt
def delete_reading_multiple_choice(request, pk):
    obj = get_object_or_404(ReadingMultipleChoice, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Reading Multiple Choice deleted successfully'
        }, status=200)
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=405)
