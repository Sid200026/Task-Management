from rest_framework import serializers
from .models import Task, TaskTracker


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        # The id and creation time should not be changed
        read_only_fields = ["id", "creation_time"]


class TaskTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTracker
        fields = "__all__"
        # The id and creation time should not be changed
        read_only_fields = ["id", "creation_time"]
