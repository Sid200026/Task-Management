from enum import Enum, unique


@unique
class TaskTypes(Enum):
    OPTIONAL = {"id": 0, "name": "Optional Task"}
    MANDATORY = {"id": 1, "name": "Mandatory Task"}
    OUTSOURCED = {"id": 2, "name": "Outsourced Task"}
    EMERGENCY = {"id": 3, "name": "Emergency Task"}


@unique
class TaskTrackerType(Enum):
    DAILY = {"id": 0, "name": "Per Day"}
    WEEKLY = {"id": 1, "name": "Per Week"}
    MONTHLY = {"id": 2, "name": "Per Month"}
