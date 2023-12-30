from rest_framework.serializers import ModelSerializer
from .models import Task


class TaskDetailSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "title", "completed", "create_ad")
        model = Task


class TaskListSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "title")
        model = Task
