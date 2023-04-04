from django.urls import path

from todo.api import views


urlpatterns = [
    path('todos', views.TodoListView.as_view(), name='todos'),
    path('todos/<int:pk>', views.TodoDetailView.as_view(), name='todo-detail'),
]

