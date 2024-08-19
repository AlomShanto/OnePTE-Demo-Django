from django.urls import path
from reading_multiple_choice.views import create_reading_multiple_choice, update_reading_multiple_choice, delete_reading_multiple_choice

app_name = 'reading_multiple_choice'

urlpatterns = [
    path('new-rmmcq-test/', create_reading_multiple_choice, name='create_test'),
    path('test/update-rmmcq/<int:pk>/', update_reading_multiple_choice, name='update_test'),
    path('test/delete-rmmcq/<int:pk>/', delete_reading_multiple_choice, name='delete_test'),
]
