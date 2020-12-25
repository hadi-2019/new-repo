from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    StudentUploadView,
    downloadcsv
)


urlpatterns = [
    path('students/', StudentListView.as_view(), name="student-list"),
    path('student/<int:pk>/', StudentDetailView.as_view(), name="student-detail"),
    path('student/create/', StudentCreateView.as_view(), name="student-create"),
    path('student/<int:pk>/edit/',
         StudentUpdateView.as_view(), name="student-update"),
    path('student/<int:pk>/delete/',
         StudentDeleteView.as_view(), name="student-delete"),

    path('upload/', StudentUploadView.as_view(), name='student-upload'),
    path('downloadcsv/', downloadcsv, name='download-csv'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
