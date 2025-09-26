from enum import Enum, StrEnum
import functools
import inspect
from typing import (
    Annotated,
    Any,
    Callable,
    Collection,
    Literal,
    LiteralString,
    Union,
    get_args,
    get_origin,
)
from typing_extensions import Doc

commands: dict[str, dict] = {}


class StatusOptions(StrEnum):
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'


class Argument:
    def __init__(
        self,
        *,
        default: Any | None = None,
        help: str | None = None,
        name_or_flags: Collection[str] | None = None,
        choices: Enum | str | None = None,
    ):
        self.default = default
        self.name_or_flags = name_or_flags
        self.choices = choices
        self.help = help

def _parameter_from_
def command[F: Callable](name: str | None = None) -> Callable[[F], F]:
    def wrap(func: F) -> F:
        cmd_name = name or func.__name__
        commands[cmd_name] = {
            'target': func,
            'help': func.__doc__,
            'args': [],
        }

        args: list[dict] = commands[cmd_name]['args']
        for param in inspect.signature(func).parameters.values():
            # NOTE: This is where to add Depends() Check
            type, *metadata = get_args(param.annotation)
            parameter = metadata.
            if get_origin(type) is Union:
                type = get_args(type)[0]
            # args.append({
            #     'name_or_flags': metadata[1:] if len(metadata)
            # })
        return func

    return wrap


@command('add')
def add_task(
    description: Annotated[str, Argument(help='A short description of the task')],
    # TODO: Enum options should be added in parens automatically for enums (and literals?)
    status: Annotated[
        StatusOptions,
        Argument(default=StatusOptions.TODO, help='The status of the task'),
    ],
) -> None:
    """Add a new task"""
    print('Adding Task...')


print(add_task.__annotations__['status'].__metadata__[0].documentation)
print(commands)
add_task('', StatusOptions.TODO)
