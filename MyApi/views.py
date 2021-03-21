from .models import ShowTodo
from .serializers import TodoSerializers
from rest_framework import generics


class TodoList(generics.ListCreateAPIView):
    queryset = ShowTodo.objects.all()
    serializer_class = TodoSerializers


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShowTodo.objects.all()
    serializer_class = TodoSerializers
