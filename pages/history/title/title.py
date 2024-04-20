from PyQt6.QtGui import QPaintEvent, QPainter, QFont
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QStyleOption, QStyle, QFrame
from PyQt6.QtCore import Qt

from components.buttons.button_border import ButtonBorder


class Title(QWidget):
    def __init__(self, parent=None):
        super(Title, self).__init__(parent)
        
        self.setFixedHeight(100)
        
        title_layout = QHBoxLayout()
        title_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        font = self.setup_font()
        
        title_text = QLabel("Історія", parent=parent)
        title_text.setFont(font)
        
        title_button_frame = QFrame(parent=parent)
        button_frame_layout = QHBoxLayout(title_button_frame)
        
        button_border = ButtonBorder(parent, "Додати новий файл")
        history_button = button_border.setup_layout()
        button_frame_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        button_frame_layout.addWidget(history_button)
        
        title_text.setObjectName("historyTitle")
        
        title_text.setAlignment(Qt.AlignmentFlag.AlignLeft)

        title_layout.addWidget(title_text)
        title_layout.addWidget(title_button_frame)
        
        self.setLayout(title_layout)
        
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