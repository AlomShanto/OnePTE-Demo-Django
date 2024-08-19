from django.urls import path
from spoken_test.views import create_spoken_text, update_spoken_text, delete_spoken_text

app_name = 'spoken_test'

urlpatterns = [
    path('new-test/', create_spoken_text, name='create_test'),
    path('test/update/<int:pk>/', update_spoken_text, name='update_test'),
    path('test/delete/<int:pk>/', delete_spoken_text, name='delete_test'),
]
