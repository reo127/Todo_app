
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.todo, name='todo'),
    path('delete_todo/<int:todo_sno>/', views.delete_todo, name='delete_todo'),
]
