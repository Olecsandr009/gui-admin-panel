from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle, QVBoxLayout, QFrame, QHBoxLayout
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional

from components.ui.buttons.button import Button
from components.ui.buttons.button import ButtonStyle


class Window(QWidget):
    # Initialize the apply widget
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(Window, self).__init__(parent)

        # Set the object name
        self.setObjectName("inputs_window")

        # Default window name
        self.title = "The text edit window"
        # Default window position
        self.top = 200
        self.left = 300
        # Default widow size
        self.width = 300
        self.height = 400

        # Default margin values
        self.margin = [16, 16, 16, 16]
        self.container = [16, 16, 16, 16]
        self.buttons = [0, 0, 0, 0]
        # Default alignment value
        self.alignment = Qt.AlignmentFlag.AlignTrailing
        self.container_alignment = Qt.AlignmentFlag.AlignJustify
        self.buttons_alignment = Qt.AlignmentFlag.AlignBottom

        self.__setupWindow()
        self.__applyStyles()
        self.__setupLayout()
        self.__configureContainer()
        self.__configureButtonsBottom()
        self.__configureButtonClose()
        self.__configureButtonApply()

        self.setLayout(self.window_layout)

    # Set the margin values
    def setContentMargins(self, left: int, top: int, right: int, bottom: int):
        self.window_layout.setContentsMargins(left, top, right, bottom)

    # Set the alignment value
    def setAlignment(self, alignment: Qt.AlignmentFlag):
        self.window_layout.setAlignment(alignment)

    # Setup the window widget
    def __setupWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)

    # Setup the widget layout
    def __setupLayout(self):
        self.window_layout = QVBoxLayout(self)
        self.window_layout.setContentsMargins(self.margin[0], self.margin[1], self.margin[2], self.margin[3])
        # self.window_layout.setAlignment(self.alignment)

    # Apply the styles
    def __applyStyles(self):
        with open("styles/styles.css", "r") as file:
            self.setStyleSheet(file.read())

    # Configure the window container
    def __configureContainer(self):
        self.window_container = QFrame(self)
        self.window_container.setObjectName("inputs_window_urls_container")

        self.container_layout = QVBoxLayout(self.window_container)
        self.container_layout.setContentsMargins(*self.container)
        # self.container_layout.setAlignment(self.container_alignment)

        self.window_layout.addWidget(self.window_container)

    # Configure the window bottom buttons
    def __configureButtonsBottom(self):
        self.buttons_bottom = QFrame(self.window_container)
        self.buttons_bottom.setObjectName("inputs_window_urls_buttons_bottom")

        self.buttons_layout = QHBoxLayout(self.buttons_bottom)
        self.buttons_layout.setContentsMargins(*self.buttons)
        self.buttons_layout.setAlignment(self.buttons_alignment)

        self.container_layout.addWidget(self.buttons_bottom)

    # Configure the window button close
    def __configureButtonClose(self):
        self.button_close = Button(self.buttons_bottom)
        self.button_close.setButtonLayout("Відмінити", ButtonStyle.BORDER)
        self.button_close.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.button_close.clicked(self._setCloseEventHandler)

        self.buttons_layout.addWidget(self.button_close)

    # Configure the window button apply
    def __configureButtonApply(self):
        self.button_apply = Button(self.buttons_bottom)
        self.button_apply.setButtonLayout("Зберегти", ButtonStyle.FILL)
        self.button_apply.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.button_apply.clicked(self._setApplyEventHandler)

        self.buttons_layout.addWidget(self.button_apply)

    # Set the mouse click event handler to the button close
    def _setCloseEventHandler(self):
        self.close()

    # Set the mouse click event handler to the button apply
    def _setApplyEventHandler(self):
        self.close()
