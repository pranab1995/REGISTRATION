from . import views
from django.urls import include, path

urlpatterns = [
    path('create/', views.add_student, name='create'),
    path('read/', views.get_student, name='read'),
    path('update/<int:id>', views.edit_student, name='update'),
    path('delete/<int:id>', views.delete_student, name='delete'),
]