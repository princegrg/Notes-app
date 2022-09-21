from django.urls import path
from . import views

urlpatterns = [
    path('notes/',views.getNotes, name = 'notes'),
    path('notes/<int:pk>/',views.getNote, name = 'note'),
    # path('notes/<int:pk>/update/',views.updateNote, name = 'update_note'),
    # path('notes/<int:pk>/delete/',views.deleteNote, name = 'delete_note'),
]


