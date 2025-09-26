from datetime import datetime
from enum import StrEnum
from typing import Annotated

from task_tracker.core import Parser


class StatusOptions(StrEnum):
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'


@Parser
class Task:
    id: Annotated[str, Field('A unique identifier for the task')]
    description: Annotated[str, 'A short description of the task']
    status: Annotated[
        StatusOptions,
        f'The status of the task ({", ".join([s for s in StatusOptions])})',
    ] = StatusOptions.TODO
    created_at: Annotated[str, 'The date and time when the task was created'] = (
        datetime.now().isoformat()
    )
    updated_at: Annotated[str, 'The date and time when the task was last updated'] = (
        datetime.now().isoformat()
    )
