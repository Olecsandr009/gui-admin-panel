from PyQt6.QtWidgets import QFrame, QVBoxLayout, QGridLayout, QLabel, QPushButton, QSizePolicy, QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QIcon, QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional
from utils.windows.item.window import Window


class GridLayout(QFrame):
    def __init__(self, filename, item, parent: Optional[QWidget] = None):
        super(QFrame, self).__init__(parent)
        self.setObjectName("gridLayout")
        
        self.window = Window()
        self.parent = parent
        self.json_data = item
        
        self.setup_layout()
        self.setup_columns()
        
        self.setLayout(self.grid_layout)

    # Setup grid layout
    def setup_layout(self):
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
    # Setup grid columns
    def setup_columns(self):
        grid_id = QLabel("№", parent=self)
        grid_name = QLabel("Ім'я:", parent=self)
        # grid_about = QLabel("Опис:", parent=self)
        grid_price = QLabel("Ціна:", parent=self)
        grid_more = QPushButton(parent=self)
        
        self.grid_layout.setColumnMinimumWidth(0, 20)
        self.grid_layout.setColumnStretch(1, 1)
        self.grid_layout.setColumnMinimumWidth(2, 100)
        self.grid_layout.setColumnMinimumWidth(3, 20)
        # self.grid_layout.setColumnMinimumWidth(4, 20)
        
        self.grid_layout.addWidget(grid_id, 0, 0)
        self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(grid_name, 0, 1)
        self.grid_layout.setSpacing(20)
        # self.grid_layout.addWidget(grid_about, 0, 2)
        # self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(grid_price, 0, 2)
        self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(grid_more, 0, 3)
        
        self.show_list(self, self.grid_layout, self.json_data)
    
    # Виведення списку
    def show_list(self, parent, grid_layout: QGridLayout, list):
        if not list: return
        
        for index, item in enumerate(list):
            grid_index = index + 1
            grid_id = QLabel(f"{grid_index}", parent=parent)
            grid_name = QLabel(item["name"], parent=parent)
            # grid_about = QLabel(item['json_about'], parent=parent)
            grid_price = QLabel(f"{item["price"]}", parent=parent)
            
            grid_more_icon = QIcon("media/icons/dots.png")
            grid_more = QPushButton(parent=parent)
            grid_more.setIcon(grid_more_icon)
            grid_more.clicked.connect(self.click_handler)
            
            # grid_about.setMaximumWidth(400)
            grid_price.setMaximumWidth(100)
            
            grid_layout.addWidget(grid_id, grid_index, 0)
            grid_layout.setSpacing(20)
            grid_layout.addWidget(grid_name, grid_index, 1)
            grid_layout.setSpacing(20)
            # grid_layout.addWidget(grid_about, grid_index, 2)
            # grid_layout.setSpacing(20)
            grid_layout.addWidget(grid_price, grid_index, 2)
            grid_layout.setSpacing(20)
            grid_layout.addWidget(grid_more, grid_index, 3)
            
    # Click handler
    def click_handler(self):
        self.window.show()
            
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)