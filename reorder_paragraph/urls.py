from django.urls import path
from reorder_paragraph.views import create_reordering_paragraph, delete_reordering_paragraph, update_reordering_paragraph

app_name = 'reorder_paragraph'

urlpatterns = [
    path('new-ro-test/', create_reordering_paragraph, name='create_test'),
    path('test/update-ro/<int:pk>/', update_reordering_paragraph, name='update_test'),
    path('test/delete-ro/<int:pk>/', delete_reordering_paragraph, name='delete_test'),
]
