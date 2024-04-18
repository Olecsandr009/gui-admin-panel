from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from pages.result_list.grid_layout.grid_layout import GridLayout


class ResultList():
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

    # Настройка елементів
    def setup_layout(self):
        result_list = QWidget(parent=self.parent)
        result_layout = QVBoxLayout(result_list)
        
        result_title = QWidget(parent=self.parent)
        result_title.setFixedHeight(100)
        title_layout = QHBoxLayout(result_title)
        title_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        font = self.setup_font()
        
        title_text = QLabel("Результат", parent=result_title)
        title_text.setFont(font)
        
        title_layout.addWidget(title_text)

        grid = GridLayout(parent=result_list)
        grid_layout = grid.setup_layout()
        
        result_layout.addWidget(result_title)
        result_layout.addWidget(grid_layout)

        return result_list
    
    # Налаштування фону
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(32)
        return font