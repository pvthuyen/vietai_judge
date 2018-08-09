from django.urls import path

from .views import upload_file, index

urlpatterns = [
    path('<int:assignment_id>/upload_file/', upload_file),
    path('', index)
]