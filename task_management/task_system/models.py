from django.db import models
from .constants import TaskTypes, TaskTrackerType


class Task(models.Model):
    task_type = models.PositiveSmallIntegerField(
        verbose_name="Type of task",
        help_text="Enter the task type",
        choices=[(tag.value["id"], tag.value["name"]) for tag in TaskTypes],
    )
    task_description = models.CharField(
        verbose_name="Task Description",
        max_length=200,
        help_text="Enter the task description",
    )
    creation_time = models.DateTimeField(verbose_name="Creation Time", auto_now=True)

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return (
            f"Task Type : {self.task_type} Description : {self.task_description[0:50]}"
        )


class TaskTracker(models.Model):
    task_type = models.PositiveSmallIntegerField(
        verbose_name="Type of task",
        help_text="Enter the task type",
        choices=[(tag.value["id"], tag.value["name"]) for tag in TaskTypes],
    )
    update_type = models.PositiveSmallIntegerField(
        verbose_name="Task tracking updation period",
        help_text="Enter the update type",
        choices=[(tag.value["id"], tag.value["name"]) for tag in TaskTrackerType],
    )
    email = models.EmailField(
        verbose_name="Email to send the task update to",
        help_text="Enter your email address",
        unique=True,
    )

    class Meta:
        verbose_name = "task tracker"
        verbose_name_plural = "task trackers"

    def __str__(self):
        return f"Task type : {self.task_type} Update Type : {self.update_type}"
