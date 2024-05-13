from .color_edit.color_edit import ColorEdit
from .line_edit.line_edit import LineEdit
from .text_edit.text_edit import TextEdit
from .urls_edit.urls_edit import UrlsEdit
# from .number_edit.number_edit import NumberEdit

from enum import Enum


class InputsScheme(Enum):
    LineEdit = 1
    TextEdit = 2
    ColorEdit = 3
    UrlsEdit = 4


__all__ = [
    "ColorEdit",
    "LineEdit",
    "TextEdit",
    "UrlsEdit",
    "InputsScheme",
    # "NumberEdit"
]
