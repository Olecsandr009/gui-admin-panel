from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QHBoxLayout
from PyQt6.QtCore import Qt

from typing import Optional

from components.ui.buttons.button import Button
from components.ui.buttons.button import ButtonStyle


class Window(QWidget):
    # Initialize the apply widget
    def __init__(self, data, key:str, parent: Optional[QWidget] = None) -> None:
        super(Window, self).__init__(parent)

        # Set object name
        self.setObjectName("inputs_window")
        
        self.data = data
        self.key = key

        # Default window name
        self.title = "The text edit window"
        # Default window position
        self.top = 200
        self.left = 300
        # Default widow size
        self.width = 300
        self.height = 400
        
        # Default margin values
        self.margin = [8, 8, 8, 8]
        # Default alignment value
        self.alignment = Qt.AlignmentFlag.AlignCenter

        self.__setupWindow()
        self.__applyStyles()
        self.__windowLayout()
        self.__configureTextEdit()
        self.__configureButtonLayout()
        self.__configureButtonClose()
        self.__configureButtonApply()
        
        
        self.buttons_bottom.setLayout(self.buttons_layout)
        self.window_layout.addWidget(self.buttons_bottom)
        
        
        self.setLayout(self.window_layout)

    # Set the margin values
    def setContentsMargins(self, left: int, top: int, right: int, bottom: int):
        self.window_layout.setContentsMargins(left, top, right, bottom)

    # Set the alignment value
    def setAlignment(self, alignment):
        self.window_layout.setAlignment(alignment)

    # Set the event handler to the button close
    def buttonCloseClickHandler(self):
        self.close()

    # Set the event handler to the button apply
    def buttonApplyClickHandler(self):
        self.data[self.key] = ""
        self.close()

    # Setup the window widget
    def __setupWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)

    # Apply the styles
    def __applyStyles(self):
        with open("styles/styles.css", "r") as file:
            self.setStyleSheet(file.read())

    # Setup the window layout
    def __windowLayout(self):
        self.window_layout = QVBoxLayout(self)
        self.window_layout.setContentsMargins(self.margin[0], self.margin[1], self.margin[2], self.margin[3])
        self.window_layout.setAlignment(self.alignment)
        
    # Configure the window text edit
    def __configureTextEdit(self):
        self.text_edit = QTextEdit(self)
        self.text_edit.setObjectName("inputs_window_text_edit")
        
        self.window_layout.addWidget(self.text_edit)
    
    # Configure the button layout
    def __configureButtonLayout(self):
        self.buttons_bottom = QWidget(self)
        self.buttons_bottom.setObjectName("inputs_window_buttons")
        
        self.buttons_layout = QHBoxLayout(self.buttons_bottom)
        self.buttons_layout.setContentsMargins(0, 30, 0, 0)
        self.buttons_layout.setAlignment(self.alignment)
        
    # Configure the button close
    def __configureButtonClose(self):
        self.button_close = Button(self.buttons_bottom)
        self.button_close.setButtonLayout("Відмінити", ButtonStyle.BORDER)
        
        self.button_close.clicked(self.buttonCloseClickHandler)
        
        self.buttons_layout.addWidget(self.button_close)
        
    # Configure the button apply
    def __configureButtonApply(self):
        self.button_apply = Button(self.buttons_bottom)
        self.button_apply.setButtonLayout("Зберегти", ButtonStyle.FILL)
        
        self.button_apply.clicked(self.buttonApplyClickHandler)
        
        self.buttons_layout.addWidget(self.button_apply)
        