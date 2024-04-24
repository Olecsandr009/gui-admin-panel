from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from pages.result_list.grid_layout.grid_layout import GridLayout


class ResultList(QWidget):
    def __init__(self, parent = None, filename:str = None):
        super(ResultList, self).__init__(parent)
        self.setObjectName("resultList")

        self.result_layout()
        
        self.title_layout()
        self.grid_layout()
        
        self.setLayout(self.result_layout)

    # Setup result layout
    def result_layout(self):
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
        
    # Setup grid layout
    def grid_layout(self):
        grid_layout = GridLayout(self)
        
        self.result_layout.addWidget(grid_layout)
    
    # Налаштування фону
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(32)
        return font