from PyQt6.QtWidgets import QFrame, QVBoxLayout, QGridLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon


class GridLayout():
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
    def setup_layout(self):
        grid_frame = QFrame(parent=self.parent)
        # grid_layout = QVBoxLayout(grid_frame)
        
        grid = QGridLayout(parent=grid_frame)
        
        grid_id = QLabel("№", parent=grid_frame)
        grid_name = QLabel("Ім'я:", parent=grid_frame)
        grid_about = QLabel("Опис:", parent=grid_frame)
        grid_price = QLabel("Ціна:", parent=grid_frame)
        
        grid_more_icon = QIcon("media/icons/dots.png")
        grid_more = QPushButton(parent=grid_frame)
        grid_more.setIcon(grid_more_icon)
        
        grid.addWidget(grid_id, 0, 0)
        grid.addWidget(grid_name, 0, 1)
        grid.addWidget(grid_about, 0, 2)
        grid.addWidget(grid_price, 0, 3)
        grid.addWidget(grid_more, 0, 4)
        
        return grid_frame