from rest_framework import status
from rest_framework.test import RequestsClient

from django.test import TestCase, Client
from django.urls import reverse

from todo.models import Todo
from todo.api.serializers import TodoSerializer

from json import dumps


class PopulateDBMixin:

    def create_todo(self):
        todo = Todo.objects.create(
            title = 'test todo',
            status = '0'
        )
        return todo


class TestTodoList(PopulateDBMixin, TestCase):

    def setUp(self):
        self.create_todo()
        self.url = 'http://127.0.0.1:8000/api/todos'
        self.client = Client()

    def test_get(self):
        response = self.client.get(self.url)
        serializer = TodoSerializer(Todo.objects.all(), many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertTrue(Todo.objects.all().count() > 0)

    def test_post(self):
        data = {'title': 'test todo #2', 'status': 1}
        response = self.client.post(self.url, data=data)
        serializer = TodoSerializer(Todo.objects.get(pk=2))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)
        self.assertTrue(Todo.objects.all().count() >= 2)


class TestTodoDetail(PopulateDBMixin, TestCase):

    def setUp(self):
        self.todo = self.create_todo()
        self.url = f'http://127.0.0.1:8000/api/todos/{self.todo.pk}'
        self.client = Client()

    def test_get(self):
        response = self.client.get(self.url)
        serializer = TodoSerializer(self.todo)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_patch(self):
        data = {'title': 'test todo #2', 'status': 0}
        response = self.client.patch(self.url, data=dumps(data), content_type='application/json')
        serializer = TodoSerializer(Todo.objects.get(pk=response.data.get('id')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)