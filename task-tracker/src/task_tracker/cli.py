from argparse import ArgumentParser
from dataclasses import dataclass, field, is_dataclass
from datetime import datetime
from enum import StrEnum
import inspect
from typing import Annotated, Any, Callable, Literal, Union, get_args, get_origin

from task_tracker.core import Parser, Requires
from task_tracker.database import Database
from task_tracker.models import Task

parser = Parser()


@command(Task)
def add_task(database: Requires[Database], task: Task) -> None:
    """Add a new task to your task list"""


def main() -> None:
    parser()
