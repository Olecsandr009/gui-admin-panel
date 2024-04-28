from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QHBoxLayout, QScrollArea, QStyleOption, QStyle
from PyQt6.QtGui import QFont, QPainter, QPaintEvent
from PyQt6.QtCore import Qt

import json

from pages.result_list.grid_layout.grid_layout import GridLayout


class ResultList(QWidget):
    def __init__(self, parent = None, filename:str = "iphone3"):
        super(ResultList, self).__init__(parent)
        self.setObjectName("resultList")
        
        self.filename = filename

        self.setup_layout()
        
        self.title_layout()
        self.scroll_area()
        self.grid_layout()
        
        self.setLayout(self.result_layout)

    # Setup result layout
    def setup_layout(self):
        self.result_layout = QVBoxLayout(self)
        self.result_layout.setContentsMargins(0, 0, 0, 0)
        
    # Setup title layout
    def title_layout(self):
        result_title = QWidget(self)
        result_title.setFixedHeight(100)
        
        title_layout = QHBoxLayout(result_title)
        title_layout.setContentsMargins(0, 0, 0, 0)
        title_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        title_text = QLabel("Результат", parent=result_title)
        title_text.setFont(self.setup_font())
        
        title_layout.addWidget(title_text)
        
        self.result_layout.addWidget(result_title)
        
    # Setup scroll area
    def scroll_area(self):
        scroll_area = QScrollArea(self)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setContentsMargins(0, 0, 0, 0)
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget(scroll_area)
        scroll_content.setObjectName("scrollWidget")
        self.scroll_layout = QVBoxLayout(scroll_content)
        
        scroll_content.setLayout(self.scroll_layout)
        
        scroll_area.setWidget(scroll_content)
        
        self.result_layout.addWidget(scroll_area)
        
    # Setup grid layout
    def grid_layout(self):
        if not self.filename: return
        
        data = []
        
        with open(f"storage/json/{self.filename}.json") as file_json:
            data = json.load(file_json)
            
        if not data: return
        
        grid_title = GridLayout(self.filename, {
            "name": "Ім'я:",
            "price": "Ціна:"
        }, "№", title=True, parent=self)
        self.scroll_layout.addWidget(grid_title)
        
        for index, item in enumerate(data):
            grid_layout = GridLayout(self.filename, item, index + 1, False, self)
            self.scroll_layout.addWidget(grid_layout)    
        
        # grid_layout = GridLayout(self.filename, data, self)
        
        
    # Налаштування фону
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(32)
        return font
    
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)