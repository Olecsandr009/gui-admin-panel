from .buttons.button import Button
from .inputs import ColorEdit, LineEdit, TextEdit, UrlsEdit, InputsScheme
from .title_text.title_text import TitleText
from .text.text import Text


class Inputs:
    ColorEdit = ColorEdit
    LineEdit = LineEdit
    TextEdit = TextEdit
    UrlsEdit = UrlsEdit
    InputsScheme = InputsScheme


__all__ = [
    "Button",
    "Inputs",
    "TitleText",
    "Text"
]
