from PyQt6.QtWidgets import QLabel, QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QPaintEvent, QPainter
from PyQt6.QtCore import Qt

from components.layout import Frame
from components.ui import Inputs, Text


class Item(Frame):
    # Initialize item
    def __init__(self, key: str, input_type: Inputs.InputsScheme, data, parent: QWidget = None):
        super(Item, self).__init__(parent)

        self.setObjectName("item_data_item")
        self.addLayout(Frame.Direction.LeftToRight)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.key = key
        self.type = input_type
        self.data = data

        self.__configureText()
        self.__configureInput()

    def __configureText(self):
        text = Text(f"{self.key}")

        self.layout.addWidget(text)
        self.layout.addSpacing(30)

    def __configureInput(self):
        input = None

        if self.type == Inputs.InputsScheme.LineEdit:
            input = Inputs.LineEdit(f"{self.key}", parent=self)
            input.setText(f"{self.data[f"{self.key}"]}")
        elif self.type == Inputs.InputsScheme.TextEdit:
            input = Inputs.TextEdit(self.data, f"{self.key}", parent=self)
            input.setText(self.data[f"{self.key}"])
        elif self.type == Inputs.InputsScheme.ColorEdit:
            input = Inputs.ColorEdit(parent=self)

            colors = self.data[f"{self.key}"]

            if len(colors):
                for color in colors:
                    input.setColor(f"{color}")

        elif self.type == Inputs.InputsScheme.UrlsEdit:
            input = Inputs.UrlsEdit(self.data, parent=self)

        self.layout.addWidget(input)

    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
