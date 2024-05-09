from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle, QVBoxLayout, QFrame, QLabel
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional

from components.ui.buttons.button import Button
from components.ui.buttons.button import ButtonStyle

from components.ui.inputs.urls_edit.window.window import Window


class UrlsEdit(QFrame):
    # Initialize the apply widget
    def __init__(self, data, parent: Optional[QWidget] = None) -> None:
        super(UrlsEdit, self).__init__(parent)

        # Set the object name
        self.setObjectName("inputs_window_urls_edit")

        self.data = data
        self.window = None

        # Default margin values
        self.margin = [0, 0, 0, 0]
        # Default alignment value
        self.alignment = Qt.AlignmentFlag.AlignLeading

        self.__setupLayout()
        self.__configureContent()
        self.__configureButton()

        self.setLayout(self.urls_layout)

    # Set the margin values
    def setContentMargins(self, left: int, top: int, right: int, bottom: int):
        self.urls_layout.setContentsMargins(left, top, right, bottom)

    # Set the alignment value
    def setAlignment(self, alignment: Qt.AlignmentFlag):
        self.urls_layout.setAlignment(alignment)

    # Setup the click event handler
    def mousePressHandler(self) -> None:
        if self.window is None:
            self.window = Window()
        self.window.show()

    # Set the text
    def setText(self, text: str):
        pass

    # Setup the widget layout
    def __setupLayout(self):
        self.urls_layout = QVBoxLayout(self)
        self.urls_layout.setContentsMargins(self.margin[0], self.margin[1], self.margin[2], self.margin[3])
        self.urls_layout.setAlignment(self.alignment)

    # Configure the content
    def __configureContent(self):
        if isinstance(self.data, str):
            self.urls_text = QLabel(text=self.data, parent=self)
            self.urls_text.setObjectName("inputs_window_urls_text")

            self.urls_layout.addWidget(self.urls_text)
        elif isinstance(self.data, list) and all(isinstance(item, str) for item in self.data):
            for index, item in enumerate(self.data):
                if index == 4: return

                if index == 3 and self.data > 3:
                    self.urls_text = QLabel(text=f"{item}...", parent=self)

                self.urls_text = QLabel(text=f"{item}", parent=self)
                self.urls_text.setObjectName("inputs_window_urls_text")

                self.urls_layout.addWidget(self.urls_text)

    # Configure the button edit
    def __configureButton(self):
        self.urls_button = Button(parent=self)
        self.urls_button.setButtonLayout("Редагувати", ButtonStyle.DEFAULT)

        self.urls_button.clicked(self.mousePressHandler)

        self.urls_layout.addWidget(self.urls_button)
