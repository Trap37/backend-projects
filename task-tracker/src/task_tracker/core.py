import inspect
from collections.abc import Callable, Collection
from enum import Enum
from typing import (
    Any,
    Union,
    cast,
    get_args,
    get_origin,
)


# NOTE: This should hold commands (later subcommands). Maybe make Command cls?
class App: ...


# FEATURE: Add __slots__ to these classes?
# FEATURE: Add __repr__ to these classes?
class Argument:
    def __init__(
        self,
        *,
        choices: Enum | str | None = None,
        help: str | None = None,
        name_or_flags: Collection[str] | None = None,
    ):
        self.choices = choices
        self.help = help
        self.name_or_flags = name_or_flags


# XXX: Can't have `None` as default value for `default` param
class Parameter:
    def __init__(
        self,
        type: Any,
        default: Any,
        help: str | None,
        name_or_flags: Collection[str] | None,
        choices: Enum | str | None,
    ):
        self.type = type
        self.default = default
        self.help = help
        self.name_or_flags = name_or_flags
        self.choices = choices


def command[F: Callable](name: str | None = None) -> Callable[[F], F]:
    def wrap(func: F) -> F:
        cmd_name = name or func.__name__
        commands[cmd_name] = {
            'target': func,
            'help': func.__doc__,
            'args': [],
        }

        args: list[dict] = commands[cmd_name]['args']
        for p in inspect.signature(func).parameters.values():
            # TODO: This is where to add Depends() Check
            type, metadata = get_args(p.annotation)
            # TODO: Can be `Argument` or `Option`
            metadata = cast(Argument, metadata)
            parameter = Parameter(
                type,
                default=p.default,
                help=metadata.help,
                name_or_flags=metadata.name_or_flags,
                choices=metadata.choices,
            )

            # TODO: This could be an `Argument` or `Option`
            if get_origin(type) is Union:
                type = get_args(type)[0]
            # args.append({
            #     'name_or_flags': metadata[1:] if len(metadata)
            # })
        return func

    return wrap
