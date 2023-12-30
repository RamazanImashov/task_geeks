from rest_framework.routers import DefaultRouter
from .views import TaskView
from django.urls import path, include

router = DefaultRouter()
router.register("task", TaskView)

urlpatterns = [
    path('', include(router.urls)),
]
