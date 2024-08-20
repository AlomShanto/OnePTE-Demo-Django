from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from reorder_paragraph.models.models import ReorderingParagraph
from reorder_paragraph.forms.forms import ReorderingParagraphForm

@csrf_exempt
def create_reordering_paragraph(request):
    if request.method == 'POST':
        form = ReorderingParagraphForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Reordering Paragraph created successfully',
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
def all_details_reordering_paragraph(request):
    if request.method == 'GET':
        objs = ReorderingParagraph.objects.all()
        data = []
        for obj in objs:
            data.append({
                'id': obj.id,
                'title': obj.title,
                'question': obj.question.split(','),  # Convert comma-separated string back to list
                'correctAns': list(map(int, obj.correctAns.split(','))) if obj.correctAns else [],  # Convert comma-separated string to list of integers, handle empty string
                'ansScript': list(map(int, obj.ansScript.split(','))) if obj.ansScript else [],  # Convert comma-separated string to list of integers, handle empty string
                'score': obj.score,
            })
        return JsonResponse({'status': 'success', 'data': data}, status=200)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def update_reordering_paragraph(request, pk):
    obj = get_object_or_404(ReorderingParagraph, pk=pk)
    if request.method == 'POST':
        form = ReorderingParagraphForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Reordering Paragraph updated successfully'
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
def delete_reordering_paragraph(request, pk):
    obj = get_object_or_404(ReorderingParagraph, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Reordering Paragraph deleted successfully'
        }, status=200)
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=405)
