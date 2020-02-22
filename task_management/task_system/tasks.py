from celery import task
from .constants import TaskTrackerType
from .models import TaskTracker
import logging

logger = logging.getLogger(__name__)


@task(name="Daily_Email")
def daily_update():
    dailyTaskTracker = TaskTrackerType.DAILY.value["id"]
    daily_update_tracker = TaskTracker.objects.filter(update_type=dailyTaskTracker)
    for tracker in daily_update_tracker:
        allTasks = tracker.getTasks()
        for _task in allTasks:
            logger.info(_task.task_description)


@task(name="Weekly_Email")
def weekly_update():
    weeklyTaskTracker = TaskTrackerType.WEEKLY.value["id"]
    weekly_update_tracker = TaskTracker.objects.filter(update_type=weeklyTaskTracker)
    for tracker in weekly_update_tracker:
        allTasks = tracker.getTasks()
        for _task in allTasks:
            logger.info(_task.task_description)


@task(name="Monthly_Email")
def monthly_update():
    monthlyTaskTracker = TaskTrackerType.MONTHLY.value["id"]
    monthly_update_tracker = TaskTracker.objects.filter(update_type=monthlyTaskTracker)
    for tracker in monthly_update_tracker:
        allTasks = tracker.getTasks()
        for _task in allTasks:
            logger.info(_task.task_description)
