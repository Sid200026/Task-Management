from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .models import Task, TaskTracker
from .serializers import TaskSerializer, TaskTrackerSerializer

logger = logging.getLogger(__name__)


@api_view(["GET"])
def apiRoot(request, format=None):
    api_info = {
        "tasks": reverse("task_system:tasks", request=request, format=format),
        "trackers": reverse("task_system:trackers", request=request, format=format),
    }
    return Response(api_info)


class TaskList(APIView):
    serializer = TaskSerializer
    model = Task

    def get(self, request, format=None):
        tasks = self.model.objects.all()
        task_serializer = self.serializer(tasks, many=True)
        return Response(task_serializer.data)

    def post(self, request, format=None):
        task_serializer = self.serializer(data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data, status=status.HTTP_201_CREATED)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    serializer = TaskSerializer
    model = Task

    def get_task_instance(self, id):
        try:
            return self.model.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id, format=None):
        task_instance = self.get_task_instance(id)
        task_serializer = self.serializer(task_instance)
        return Response(task_serializer.data)

    def put(self, request, id, format=None):
        task_instance = self.get_task_instance(id)
        task_serializer = self.serializer(task_instance, data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        task_instance = self.get_task_instance(id)
        task_serializer = self.serializer(task_instance)
        task_instance.delete()
        return Response(task_serializer.data, status=status.HTTP_204_NO_CONTENT)


class TaskTrackerList(APIView):
    serializer = TaskTrackerSerializer
    model = TaskTracker

    def get(self, request, format=None):
        task_trackers = self.model.objects.all()
        task_tracker_serializer = self.serializer(task_trackers, many=True)
        return Response(task_tracker_serializer.data)

    def post(self, request, format=None):
        task_tracker_serializer = self.serializer(data=request.data)
        if task_tracker_serializer.is_valid():
            task_tracker_serializer.save()
            return Response(
                task_tracker_serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            task_tracker_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class TaskTrackerDetail(APIView):
    serializer = TaskTrackerSerializer
    model = TaskTracker

    def get_task_instance(self, id):
        try:
            return self.model.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id, format=None):
        task_tracker_instance = self.get_task_instance(id)
        task_tracker_serializer = self.serializer(task_tracker_instance)
        return Response(task_tracker_serializer.data)

    def put(self, request, id, format=None):
        task_tracker_instance = self.get_task_instance(id)
        task_tracker_serializer = self.serializer(
            task_tracker_instance, data=request.data
        )
        if task_tracker_serializer.is_valid():
            task_tracker_serializer.save()
            return Response(task_tracker_serializer.data)
        return Response(
            task_tracker_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id, format=None):
        task_tracker_instance = self.get_task_instance(id)
        task_tracker_serializer = self.serializer(task_tracker_instance)
        task_tracker_instance.delete()
        return Response(task_tracker_serializer.data, status=status.HTTP_204_NO_CONTENT)
