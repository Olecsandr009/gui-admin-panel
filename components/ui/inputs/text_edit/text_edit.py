from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle, QFrame, QVBoxLayout, QTextEdit, QLabel
from PyQt6.QtGui import QMouseEvent, QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional, List
from abc import ABC, abstractmethod

from components.ui.inputs.text_edit.window.window import Window


class TextEditInterface(ABC):
    # Add the observer
    @abstractmethod
    def attach(self, observer: "Observer") -> None:
        pass

    # Remove the observer
    @abstractmethod
    def detach(self, observer: "Observer") -> None:
        pass


class Observer(ABC):
    # Receive update from text edit
    @abstractmethod
    def update(self, text: TextEditInterface) -> None:
        pass


class TextEdit(QFrame):
    # Initialize the apply widget
    def __init__(self, data=None, key: str = None, parent: Optional[QWidget] = None) -> None:
        super(TextEdit, self).__init__(parent)

        # Set object name
        self.setObjectName("inputs_text_edit")

        self.data = data
        self.key = key
        self.window = None

        # Default margin values
        self.margin = [0, 0, 0, 0]
        # Default alignment value
        self.alignment = Qt.AlignmentFlag.AlignLeading

        self.__textEditLayout()
        # self.__configureLineEdit()

        self.setLayout(self.text_layout)

    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)

    # Setup the click event handler
    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        if self.data and event.button() == Qt.MouseButton.LeftButton:
            if self.window is None:
                self.window = Window(self.data, self.key)
            self.window.show()
        return super().mousePressEvent(event)

    # Set the margin values
    def setContentsMargins(self, left: int, top: int, right: int, bottom: int):
        self.text_layout.setContentsMargins(left, top, right, bottom)

    # Set the alignment values
    def setAlignment(self, alignment):
        self.text_layout.setAlignment(alignment)

    # Set the placeholder text
    def setPlaceholderText(self, text: str):
        self.text_edit.setPlaceholderText(text)

    # Set the fixed height value
    def setFixedHeight(self, h: int) -> None:
        return super().setFixedHeight(h)

    # Set the text row
    def setText(self, text: str) -> None:
        self.text_value = QLabel(f"{text[:50]}...", self)
        self.text_value.setObjectName("inputs_text_edit_value")
        self.text_layout.addWidget(self.text_value)

    # Setup the text edit layout
    def __textEditLayout(self):
        self.text_layout = QVBoxLayout(self)
        self.text_layout.setContentsMargins(self.margin[0], self.margin[1], self.margin[2], self.margin[3])
