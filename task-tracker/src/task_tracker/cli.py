from enum import StrEnum
from typing import Annotated
from task_tracker.core import command, Argument


class StatusOptions(StrEnum):
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'


@command('add')
def add_task(
    description: Annotated[str, Argument(help='A short description of the task')],
    # TODO: Enum options should be added in parens automatically for enums (and literals?)
    status: Annotated[
        StatusOptions,
        Argument(help='The status of the task'),
    ] = StatusOptions.TODO,
) -> None:
    """Add a new task"""
    print('Adding Task...')


# print(add_task.__annotations__['status'].__metadata__[0].documentation)
# print(commands)
# add_task('', StatusOptions.TODO)
