from django.utils import timezone

import datetime
import calendar

from .constants import TaskTrackerType

"""
This function takes 3 parameters
1. end_date : When the function was called
2. created_date : When the task tracker was created
3. update_type : daily, weekly or monthly update
"""


def get_start_date(
    end_date=timezone.now(),
    created_date=timezone.now(),
    update_type=TaskTrackerType.DAILY.name,
):
    start_date = None
    update_days = 0
    if update_type is TaskTrackerType.DAILY.name:
        update_days = 1
    elif update_type is TaskTrackerType.WEEKLY.name:
        update_days = 7
    elif update_type is TaskTrackerType.MONTHLY.name:
        current_month = end_date.month
        required_year = end_date.year
        # If month is January the required year is the previous year
        if current_month == 1:
            required_year -= 1
        update_days = calendar.monthrange(required_year, current_month - 1)[1]
    start_date = end_date - datetime.timedelta(days=update_days)
    # if the start date calculated is before the date when the tracker was created then change
    # start date to the date tracker was created
    if start_date < created_date:
        start_date = created_date
    return start_date
