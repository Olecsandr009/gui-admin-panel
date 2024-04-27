from PyQt6.QtWidgets import QGridLayout, QWidget, QLabel, QPushButton, QStyleOption, QStyle, QFrame
from PyQt6.QtGui import QIcon, QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional

from utils.windows.item.window import Window


class GridLayout(QFrame):
    def __init__(self, filename, item, id, title = False, parent: Optional[QWidget] = None):
        super(GridLayout, self).__init__(parent)
        self.setObjectName("result-grid")
        
        self.window = Window()
        self.parent = parent
        self.item_data = item
        self.id = id
        self.title = title
        
        self.setup_layout()
        self.grid_columns()
        
        self.setLayout(self.grid_layout)
        
    # Setup grid layout
    def setup_layout(self):
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
    # Setup grid columns
    def grid_columns(self):
        grid_id = QLabel(str(self.id), parent=self.parent)
        grid_name = QLabel(self.item_data["name"], parent=self.parent)
        # grid_about = QLabel("Опис:", parent=self)
        # grid_about.setMaximumWidth(400)
        grid_price = QLabel(str(self.item_data["price"]), parent=self.parent)
        grid_price.setMaximumWidth(100)
        
        grid_more = QPushButton(parent=self.parent)
        grid_more.setFixedWidth(20)
        
        if not self.title:
            grid_more_icon = QIcon("media/icons/dots.png")
            grid_more.setIcon(grid_more_icon)
            grid_more.clicked.connect(self.click_handler)
        
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