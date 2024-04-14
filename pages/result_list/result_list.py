from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame

from pages.result_list.grid_layout.grid_layout import GridLayout


class ResultList():
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

    # Настройка елементів
    def setup_layout(self):
        result_list = QWidget(parent=self.parent)
        result_layout = QVBoxLayout(result_list)

        grid = GridLayout(parent=result_list)
        grid_layout = grid.setup_layout()
        
        result_layout.addWidget(grid_layout)

        return result_list