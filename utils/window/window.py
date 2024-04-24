from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QTabWidget, QVBoxLayout, QStackedWidget, QPushButton

from PyQt6.QtCore import Qt

from components.sidebar.sidebar import Sidebar
from components.title_bar.title_bar import TitleBar
from components.footer.footer import Footer

from pages.result_list.result_list import ResultList
from pages.test_tab.test_tab import TestTab
from pages.history.history import History

from utils.stacked_nav.stacked_nav import StackedNav


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.title = "GUI Admin panel"
        self.top = 100
        self.left = 200
        self.width = 1000
        self.height = 600
        self.stack = QStackedWidget()
        
        self.sidebar_items = [
            "Всі товари",
            "Добавить новий",
            "Історія"
        ]
        
        self.footer_data = {
                "author": "Oleksandr",
                "type": "Json"
        }
        
        self.files_list = []

        self.apply_styles()
        self.setup_ui()

        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        
        self.central_widget = QWidget(parent=self)
        self.central_layout = QHBoxLayout(self.central_widget)
        self.central_layout.setContentsMargins(0, 0, 0, 0)

        self.content = QWidget(parent=self.central_widget)
        self.content.setObjectName("content")
        self.content_layout = QVBoxLayout(self.content)
        
        title_bar = TitleBar(parent=self.content, main=self)
        title_layout = title_bar.setup_layout()
        
        footer = Footer(data=self.footer_data, parent=self.content)
        
        result_list = ResultList(parent=self.content)
        
        test_tab = TestTab(parent=self.content)
        
        history = History(parent=self.content, stack=self.stack)
        
        self.stack.addWidget(result_list)
        self.stack.addWidget(test_tab)
        self.stack.addWidget(history)
        
        self.content_layout.addWidget(title_layout)
        self.content_layout.addWidget(self.stack)
        self.content_layout.addWidget(footer)
        
        self.sidebar = Sidebar(parent=self, list=self.sidebar_items, stack=self.stack)
        self.central_layout.addWidget(self.sidebar)
        self.central_layout.addWidget(self.content)
        
        self.setCentralWidget(self.central_widget)
        
    # Зміна стану вікна
    def toggle_maximized(self):
        print('click')
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
            
    # Підключення стилів головного вікна
    def apply_styles(self):
        self.setObjectName('admin-window')
        self.setProperty('class', 'admin-window')   

        with open("styles/styles.css", "r") as file:
            self.setStyleSheet(file.read())
            
    # Налаштування вигляду головного вікна
    def setup_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)