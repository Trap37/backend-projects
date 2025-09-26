# def _get_metadata(obj: Callable):
#     # NOTE: This could work for any class passed instead of only dataclasses
#     if is_dataclass(obj):
#         func = obj.__init__
#     else:
#         func = obj

#     for param in inspect.signature(func).parameters.values():
#         # the self param is unneeded
#         if param.name == 'self':
#             continue

#         type, *metadata = get_args(param.annotation)
#         if get_origin(type) is Union:
#             print(f'`type` is `Union`: {type} {metadata}')
#             type = get_args(type)[0]

from argparse import ArgumentParser
from dataclasses import dataclass
from typing import Callable, dataclass_transform


class Requires[T]:
    required: T


class Field:
    def __init__(self, help: str | None = None, init: bool = False):
        pass


class Parser:
    def __init__(self):
        self._parser = ArgumentParser()

    def __call__(self, *args):
        self._parser.parse_args(args)

    @dataclass_transform(kw_only_default=True)
    def parser[T](cls: T):
        return dataclass(cls, kw_only=True)

    def command(uses: Callable | None = None):
        def wraps(func: Callable): ...

from typing_extensions import Doc