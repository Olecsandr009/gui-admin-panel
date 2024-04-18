from PyQt6.QtWidgets import QFrame, QVBoxLayout, QGridLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from components.json.json import Json


class GridLayout():
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
    # Показати пункт
    def show_item(self, item, title=False):
        grid_frame = QFrame(parent=self.parent)
        grid_layout = QGridLayout(grid_frame)
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        grid_id = QLabel(item["file_id"], parent=grid_frame)
        grid_id.setObjectName("historyText")
        grid_name = QLabel(item["file_name"], parent=grid_frame)
        grid_name.setObjectName("historyText")
        grid_date = QLabel(item["last_change"], parent=grid_frame)
        grid_date.setObjectName("historyText")
        grid_size = QLabel(item["file_size"], parent=grid_frame)
        grid_size.setObjectName("historyText")
        grid_type = QLabel(item["file_type"], parent=grid_frame)
        grid_type.setObjectName("historyText")
        
        grid_delete = QPushButton(parent=grid_frame)
        grid_delete.setFixedWidth(20)
        
        if not title:
            grid_icon = QIcon("media/icons/trash.png")
            grid_delete.setIcon(grid_icon)
        
        grid_layout.setColumnMinimumWidth(0, 20)
        grid_layout.setColumnStretch(1, 1)
        grid_layout.setColumnMinimumWidth(2, 100)
        grid_layout.setColumnMinimumWidth(3, 100)
        grid_layout.setColumnMinimumWidth(4, 100)
        grid_layout.setColumnMinimumWidth(5, 20)
                            
        grid_layout.addWidget(grid_id, 0, 0)
        grid_layout.setSpacing(20)
        grid_layout.addWidget(grid_name, 0, 1)
        grid_layout.setSpacing(20)
        grid_layout.addWidget(grid_date, 0, 2)
        grid_layout.setSpacing(20)
        grid_layout.addWidget(grid_size, 0, 3)
        grid_layout.setSpacing(20)
        grid_layout.addWidget(grid_type, 0, 4)
        grid_layout.setSpacing(20)
        grid_layout.addWidget(grid_delete, 0, 5)
        
        return grid_frame
            
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