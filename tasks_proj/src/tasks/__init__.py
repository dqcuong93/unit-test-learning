"""Minimal Project Task Management."""

from .api import (  # noqa: F401
    Task,
    TasksException,
    add,
    count,
    delete,
    delete_all,
    get,
    list_tasks,
    start_tasks_db,
    stop_tasks_db,
    unique_id,
    update,
)

__version__ = "0.1.0"
