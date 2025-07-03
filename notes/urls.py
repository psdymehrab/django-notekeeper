from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path('add/', views.add_note, name='add_note'),
    path('', views.note_view, name='note_list'),
    path('del/<int:note_id>', views.delete_note, name='note_delete'),
    path('update/<int:note_id>', views.update_note, name='note_update'),
]