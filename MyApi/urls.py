from .views import TodoList, DetailTodo
from django.urls import path

urlpatterns = [
    path('', TodoList.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
]