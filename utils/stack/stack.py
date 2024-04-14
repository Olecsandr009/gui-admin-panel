from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

# Сторінки
from pages.result_list.result_list import ResultList
from pages.test_tab.test_tab import TestTab

class Stack(QWidget):
    def __init__(self, stack: QStackedWidget):
        super().__init__()

        self.stack = stack
        
        self.setup_layout()

    # Налаштування stack Widgets
    def setup_layout(self):

        page1 = ResultList()
        page2 = TestTab()
        
        self.stack.addWidget(page1)
        self.stack.addWidget(page2)
        
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)