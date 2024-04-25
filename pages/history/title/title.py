from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QStyleOption, QStyle, QFrame
from PyQt6.QtGui import QPaintEvent, QPainter, QFont
from PyQt6.QtCore import Qt

from components.buttons.button_border import ButtonBorder

from dataclasses import dataclass
from typing import Optional


@dataclass
class TitleData:
    pass

class Title(QWidget):
    def __init__(self, parent=None):
        super(Title, self).__init__(parent)
        self.setObjectName("historyTitle")
        self.setFixedHeight(100)
        
        self.setup_layout()
        
        self.text_widget()
        self.button_layout()
        
        self.setLayout(self.title_layout)
        
    # Setup title layout
    def setup_layout(self):
        self.title_layout = QHBoxLayout(self)
        self.title_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        
    # Setup text widget
    def text_widget(self):        
        title_text = QLabel("Історія", parent=self)
        title_text.setObjectName("titleText")
        title_text.setFont(self.setup_font())
        title_text.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.title_layout.addWidget(title_text)
        
    # Setup button layout
    def button_layout(self):        
        title_button = QFrame(parent=self)
        title_button.setObjectName("buttonLayout")
        
        button_layout = QHBoxLayout(title_button)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        button_border = ButtonBorder(None, "Додати новий файл", title_button )
        button_layout.addWidget(button_border)
        
        self.title_layout.addWidget(title_button)

    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
    
    # Налаштування фону
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(32)
        return font