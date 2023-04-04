from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from todo.models import Todo
from todo.api.serializers import TodoSerializer


class TodoListView(ListCreateAPIView):
    model = Todo
    queryset = model.objects.all()
    serializer_class = TodoSerializer


class TodoDetailView(RetrieveUpdateDestroyAPIView):
    model = Todo
    queryset = model.objects.all()
    serializer_class = TodoSerializer

