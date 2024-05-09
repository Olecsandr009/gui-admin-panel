from PyQt6.QtWidgets import QFrame, QPushButton, QStyleOption, QStyle, QWidget, QVBoxLayout
from PyQt6.QtGui import QFont, QPainter, QPaintEvent, QCursor
from PyQt6.QtCore import Qt, pyqtSlot

from enum import Enum

from typing import Optional

from components.ui.buttons.button_border import ButtonBorder
from components.ui.buttons.button_fill import ButtonFill
from components.ui.buttons.button_default import ButtonDefault


class ButtonStyle(Enum):
    DEFAULT = 1
    BORDER = 2
    FILL = 3


class Button(QFrame):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(Button, self).__init__(parent)

        # Set the object name
        self.setObjectName("button")

        # Default margin values
        self.margin = [0, 0, 0, 0]
        # Default alignment value
        self.alignment = Qt.AlignmentFlag.AlignLeading
        # Default button var
        self.button = None

        self.__setupLayout()

        self.setLayout(self.button_layout)

    # Set the margin values
    def setContentMargins(self, left: int, top: int, right: int, bottom: int):
        self.button_layout.setContentsMargins(left, top, right, bottom)

    @pyqtSlot()
    def clicked(self, slot):
        if self.button: self.button.clicked.connect(slot)

    # Set the button layout
    def setButtonLayout(self, text: str, style: ButtonStyle):
        self.button = None

        if style == ButtonStyle.BORDER:
            self.button = ButtonBorder(text=text, parent=self)
        elif style == ButtonStyle.FILL:
            self.button = ButtonFill(text=text, parent=self)
        elif style == ButtonStyle.DEFAULT:
            self.button = ButtonDefault(text=text, parent=self)

        if self.button:
            self.button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.button_layout.addWidget(self.button)

    # Set the alignment value
    def setAlignment(self, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeading):
        self.button_layout.setAlignment(alignment)

    # Set the text font
    def setFont(self, font: QFont) -> None:
        self.button.setFont(font)

    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)

    # Setup the layout
    def __setupLayout(self):
        self.button_layout = QVBoxLayout(self)
        self.button_layout.setContentsMargins(self.margin[0], self.margin[1], self.margin[2], self.margin[3])
        self.button_layout.setAlignment(self.alignment)
