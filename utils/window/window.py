from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QTabWidget, QVBoxLayout, QStackedWidget, QPushButton

from PyQt6.QtCore import Qt

from components.sidebar.sidebar import Sidebar
from components.title_bar.title_bar import TitleBar
from components.footer.footer import Footer
from pages.result_list.result_list import ResultList
from pages.test_tab.test_tab import TestTab

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "GUI Admin panel"
        self.top = 100
        self.left = 200
        self.width = 1000
        self.height = 600
        
        self.sidebar_item = [
            "Всі товари",
            "Добавить новий",
            "Історія"
        ]

        self.setup_ui()
        self.apply_styles()
        self.setup_layout()
        
    # Налаштування вигляду головного вікна
    def setup_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    # Підключення стилів головного вікна
    def apply_styles(self):
        self.setObjectName('admin-window')
        self.setProperty('class', 'admin-window')   

        with open("styles/styles.css", "r") as file:
            self.setStyleSheet(file.read())

    # Налаштування елементів головного вікна
    def setup_layout(self):
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        stackWidget = QStackedWidget()
        
        self.central_widget = QWidget(parent=self)
        self.central_layout = QHBoxLayout(self.central_widget)
        self.central_layout.setContentsMargins(0, 0, 0, 0)

        self.sidebar = Sidebar(parent=self.central_widget, stack=stackWidget)
        
        self.content = QWidget(parent=self.central_widget)
        self.content.setObjectName("content")
        self.content_layout = QVBoxLayout(self.content)
        
        title_bar = TitleBar(parent=self.content, main=self)
        title_layout = title_bar.setup_layout()
        
        result_list = ResultList(parent=self.content)
        result_layout = result_list.setup_layout()
        
        test_tab = TestTab(parent=self.content)
        test_layout = test_tab.setup_layout()
        
        footer = Footer(parent=self.content)
        footer_layout = footer.setup_layout()
        
        stackWidget.addWidget(result_layout)
        stackWidget.addWidget(test_layout)
        
        self.content_layout.addWidget(title_layout)
        self.content_layout.addWidget(stackWidget)
        self.content_layout.addWidget(footer_layout)
        
        self.central_layout.addWidget(self.sidebar.setup_layout())
        self.central_layout.addWidget(self.content)
        
        self.setCentralWidget(self.central_widget)
        
    # Зміна стану вікна
    def toggle_maximized(self):
        print('click')
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()