from django.urls import path, include
from .mypaginations import MyCursorPagination

from .views import DesignationListAPIView, TodoListCreate, TodoUpdateDelete

urlpatterns = [
    path("designations/", DesignationListAPIView.as_view(), name="designations-list"),

    path('todo/', TodoListCreate.as_view()),
    path('todo/<int:pk>/', TodoUpdateDelete.as_view()),

]