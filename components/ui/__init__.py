from .buttons.button import Button
from .inputs import ColorEdit, LineEdit, TextEdit, UrlsEdit
from .title_text.title_text import TitleText

class Inputs:
    ColorEdit = ColorEdit
    LineEdit = LineEdit
    TextEdit = TextEdit
    UrlsEdit = UrlsEdit


__all__ = [
    "Button",
    "Inputs",
    "TitleText"
]
