from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QPushButton, QTabWidget
from sidebar.sidebar import Sidebar
from result_list.result_list import ResultList


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "GUI Admin panel"
        self.top = 100
        self.left = 200
        self.width = 1000
        self.height = 600

        self.tabs = QTabWidget()
        
        self.setup_ui()
        self.apply_styles()
        self.setup_layout()

    # Налаштування вигляду головного вікна
    def setup_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tabs.setTabBarAutoHide(True)

    # Підключення стилів головного вікна
    def apply_styles(self):
        self.setObjectName('admin-window')
        self.setProperty('class', 'admin-window')
        
        with open("window/window.css", "r") as file:
            self.setStyleSheet(file.read())

    # Налаштування елементів головного вікна
    def setup_layout(self):
        layout = QHBoxLayout()

        # Sidebar
        sidebar = Sidebar(self.tabs)
        layout.addWidget(sidebar)

        # Result list
        result_list = ResultList()
        self.tabs.addTab(result_list, "result list")

        layout.addWidget(self.tabs)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)
        