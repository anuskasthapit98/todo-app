
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import generics

from dashboard.models import Designation, Todo
from .serializers import DesignationSerializer, TodoSerializer
from .mypaginations import MyCursorPagination

class DesignationListAPIView(ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class TodoListCreate( generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = MyCursorPagination

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class TodoUpdateDelete( generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = MyCursorPagination

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)