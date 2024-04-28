from PyQt6.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton, QStackedWidget, QStyleOption, QStyle
from PyQt6.QtGui import QIcon, QMouseEvent, QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from pages.result_list.result_list import ResultList

class GridLayout(QFrame):
    def __init__(self, parent, item, stack: QStackedWidget, title=False):
        super(GridLayout, self).__init__(parent)
        self.setObjectName("historyItem")
        self.stack = stack
        self.item = item
        self.title = title
        
        self.grid_layout()
        self.grid_columns()
        
        self.setLayout(self.grid_layout)
        
    # Setup grid layout
    def grid_layout(self):
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 8, 0, 8)
        self.grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
    # Setup grid columns
    def grid_columns(self):
        grid_id = QLabel(self.item["file_id"], parent=self)
        grid_id.setObjectName("historyText")
        grid_name = QLabel(self.item["file_name"], parent=self)
        grid_name.setObjectName("historyText")
        grid_date = QLabel(self.item["last_change"], parent=self)
        grid_date.setObjectName("historyText")
        grid_size = QLabel(self.item["file_size"], parent=self)
        grid_size.setObjectName("historyText")
        grid_type = QLabel(self.item["file_type"], parent=self)
        grid_type.setObjectName("historyText")
        
        grid_delete = QPushButton(parent=self)
        grid_delete.setFixedWidth(20)
        
        if not self.title:
            grid_icon = QIcon("media/icons/trash.png")
            grid_delete.setIcon(grid_icon)
            
            grid_delete.clicked.connect(self.onPressDelete)
        
        self.grid_layout.setColumnMinimumWidth(0, 20)
        self.grid_layout.setColumnStretch(1, 1)
        self.grid_layout.setColumnMinimumWidth(2, 100)
        self.grid_layout.setColumnMinimumWidth(3, 100)
        self.grid_layout.setColumnMinimumWidth(4, 100)
        self.grid_layout.setColumnMinimumWidth(5, 20)
                            
        self.grid_layout.addWidget(grid_id, 0, 0)
        self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(grid_name, 0, 1)
        self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(grid_date, 0, 2)
        self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(grid_size, 0, 3)
        self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(grid_type, 0, 4)
        self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(grid_delete, 0, 5)
        
        self.setLayout(self.grid_layout)
        
    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            print("press mouse in self.item")
            self.stack.setCurrentWidget(ResultList(parent=None, filename=self.item["file_name"]))
        return super().mousePressEvent(event)
    
    def onPressDelete(self) -> None:
        print("press")
        
    # Отримання рядка сітки
    def get_row_widgets(self, grid_layout:QGridLayout, row: int):
        widgets = []
        for column_index in range(grid_layout.columnCount()):
            item = grid_layout.itemAtPosition(row, column_index)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widgets.append(widget)
        return widgets
    
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)