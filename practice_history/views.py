from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from practice_history.forms.forms import SubmissionHistoryForm
from practice_history.models.models import SubmissionHistory
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def practice_history(request, user_id):
    if request.method == 'GET':
        user = get_object_or_404(User, pk=user_id)  # Get the user by ID or return 404
        submissions = SubmissionHistory.objects.filter(user=user).order_by('-timestamp')
        data = [{
            'exam_type': submission.exam_type,
            'question_id': submission.question_id,
            'timestamp': submission.timestamp.isoformat(),  # Convert timestamp to ISO 8601 format
        } for submission in submissions]
        return JsonResponse({'status': 'success', 'data': data}, status=200)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def create_new_submission(request):
    if request.method == 'POST':
        form = SubmissionHistoryForm(request.POST)
        if form.is_valid():
            submission = form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Submission history created successfully.',
                'data': {
                    'user': submission.user.username,  # or user.id depending on your needs
                    'exam_type': submission.exam_type,
                    'question_id': submission.question_id,
                    'timestamp': submission.timestamp,
                }
            }, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
