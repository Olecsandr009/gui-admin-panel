from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QTabWidget, QVBoxLayout, QStackedWidget, QPushButton
from PyQt6.QtCore import Qt, QPoint, QPointF

from components.sidebar.sidebar import Sidebar
from components.title_bar.title_bar import TitleBar
from components.footer.footer import Footer

from pages.result_list.result_list import ResultList
from pages.test_tab.test_tab import TestTab
from pages.history.history import History


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.title = "GUI Admin panel"
        self.top = 50
        self.left = 100
        self.width = 1200
        self.height = 800
        
        self.old_pos = None
        
        self.stack_widget = QStackedWidget()
        
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
        
        self.setupCentralWidget()

        self.sidebar_layout()
        self.content_layout()
        
        self.setCentralWidget(self.window_widget)
        
    # Setup central widget
    def setupCentralWidget(self):
        self.window_widget = QWidget(self)
        self.window_layout = QHBoxLayout(self.window_widget)
        self.window_layout.setContentsMargins(0, 0, 0, 0)
            
    # Setup sidebar layout
    def sidebar_layout(self):
        sidebar_layout = Sidebar(parent=self, list=self.sidebar_items, stack=self.stack_widget)
        self.window_layout.addWidget(sidebar_layout)
        
    # Setup content layout
    def content_layout(self):
        content = QWidget(self)
        content.setObjectName("content")
        
        content_layout = QVBoxLayout(content)
            
        # Title bar layout
        title_bar = TitleBar(main=self, parent=content)
        content_layout.addWidget(title_bar)
        
        
        # Result list layout stack
        result_list = ResultList(parent=content)
        self.stack_widget.addWidget(result_list)
        
        # Test tab layout stack
        test_tab = TestTab(parent=content)
        self.stack_widget.addWidget(test_tab)
        
        # History layout stack
        history = History(parent=content, stack=self.stack_widget)
        self.stack_widget.addWidget(history)
        
        content_layout.addWidget(self.stack_widget)
        
        # Footer layout
        footer = Footer(data=self.footer_data, parent=content)
        content_layout.addWidget(footer)
        
        self.window_layout.addWidget(content)
        
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
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPosition() - self.old_pos
            new_pos = self.pos() + QPoint(int(delta.x()), int(delta.y()))
            self.move(new_pos)
            self.old_pos = event.globalPosition()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = None