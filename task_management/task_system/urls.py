from django.urls import path, re_path
from .views import TaskList, TaskDetail, apiRoot, TaskTrackerList, TaskTrackerDetail
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "task_system"

urlpatterns = [
    path("", apiRoot, name="api_root"),
    path("tasks/", TaskList.as_view(), name="tasks"),
    path("tasks/<int:id>", TaskDetail.as_view(), name="task"),
    path("track/", TaskTrackerList.as_view(), name="trackers"),
    path("track/<int:id>", TaskTrackerDetail.as_view(), name="task"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
