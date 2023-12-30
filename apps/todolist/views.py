from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskListSerializer, TaskDetailSerializer

# Create your views here.


class TaskView(ModelViewSet):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        return TaskDetailSerializer
