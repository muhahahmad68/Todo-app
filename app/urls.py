from django.urls import path
from .views import TaskDelete, TaskDetail, TaskList, TaskCreate, TaskUpdate

urlpatterns = [
    path("", TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    path('task-edit/<int:pk>', TaskUpdate.as_view(), name='task-edit'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]
