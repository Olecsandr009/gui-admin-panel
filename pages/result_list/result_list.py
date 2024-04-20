from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from pages.result_list.grid_layout.grid_layout import GridLayout


class ResultList(QWidget):
    def __init__(self, parent = None, filename:str = None):
        super(ResultList, self).__init__(parent)

        result_layout = QVBoxLayout(self)
        
        result_title = QWidget(self)
        result_title.setFixedHeight(100)
        title_layout = QHBoxLayout(result_title)
        title_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        font = self.setup_font()
        
        title_text = QLabel("Результат", parent=result_title)
        title_text.setFont(font)
        
        title_layout.addWidget(title_text)

        grid = GridLayout(parent=self)
        grid_layout = grid.setup_layout()
        
        result_layout.addWidget(result_title)
        result_layout.addWidget(grid_layout)

        self.setLayout(result_layout)
    
    # Налаштування фону
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(32)
        return font