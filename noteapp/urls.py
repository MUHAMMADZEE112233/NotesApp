from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteListAPI.as_view(), name='note-list-api'),
    path('<int:pk>/', views.NoteDetailAPI.as_view(), name='note-detail-api'),
    path('summarize/<int:notes_id>/', views.SummarizeTextView.as_view(), name='summarize-text'),
]
