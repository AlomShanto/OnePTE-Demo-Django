from django.urls import path
from practice_history.views import practice_history, create_new_submission

app_name = 'practice_history'

urlpatterns = [
    path('history/<int:user_id>/', practice_history, name='practice_history'),
    path('create-new-submission/', create_new_submission, name='create_new_submission'),
]
