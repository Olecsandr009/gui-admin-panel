from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPainter, QPaintEvent, QMouseEvent
from PyQt6.QtCore import Qt

from typing import Optional

from components.ui.inputs.color_edit.window.window import Window


class ColorEdit(QWidget):
    # Initialize the apply widget
    def __init__(self, parent: Optional[QWidget]) -> None:
        super(ColorEdit, self).__init__(parent)

        # Set the object name
        self.setObjectName("inputs_color_edit")

        self.window = None

        # Default margin values
        self.margin = [0, 0, 0, 0]
        # Default alignment value
        self.alignment = Qt.AlignmentFlag.AlignLeading

        self.__setupLayout()

        self.setLayout(self.color_layout)

    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)

    # Set the margin values
    def setContentMargins(self, left: int, top: int, right: int, bottom: int):
        self.color_layout.setContentsMargins(left, top, right, bottom)

    # Set the alignment value
    def setAlignment(self, alignment: Qt.AlignmentFlag):
        self.color_layout.setAlignment(alignment)

    # Setup the click event handler
    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        if self.data and event.button() == Qt.MouseButton.LeftButton:
            if self.window is None:
                self.window = Window(self.data, self.key)
            self.window.show()
        return super().mousePressEvent(event)

    # Set the color edit
    def setColor(self, color: str):
        self.color_edit = QPushButton(self)
        self.color_edit.setObjectName("inputs_color_edit_button")
        self.color_edit.setStyleSheet(f"background-color: {color}")

        self.color_edit.clicked.connect(self.__setupClickHandler)

        self.color_layout.addWidget(self.color_edit)

    # Setup the event handler to the button click
    def __setupClickHandler(self):
        if self.window is None:
            self.window = Window()
        self.window.show()

    # Setup the widget layout
    def __setupLayout(self):
        self.color_layout = QHBoxLayout(self)
        self.color_layout.setContentsMargins(self.margin[0], self.margin[1], self.margin[2], self.margin[3])
        self.color_layout.setAlignment(self.alignment)
