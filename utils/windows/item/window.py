from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QFrame, QStackedWidget, QVBoxLayout, QLabel, QPlainTextEdit, QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap

import requests
from utils.windows.item.tools.tools import Tools
from utils.image.image import Image
from typing import Optional
import json


class Window(QMainWindow):
    def __init__(self, filename = None, name = None, parent: Optional[QWidget] = None):
        super(Window, self).__init__(parent)
        self.title = "Item window"
        self.top = 200
        self.left = 300
        self.width = 1200
        self.height = 800
        
        self.filename = "iphone3"
        self.name = "Мобільний телефон Apple iPhone 15 Pro Max 256GB Natural Titanium (MU793RX/A)"
        
        self.data = None
        
        self.get_data()
        
        self.apply_styles()
        self.setup_window()
        self.setup_layout()
        self.setup_media()
        self.setup_content()
        
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)
        
    # Apply styles
    def apply_styles(self):
        self.setObjectName("item-window")
        self.setProperty('class', 'item-window')   

        with open("styles/styles.css", "r") as file:
            self.setStyleSheet(file.read())
    
    # Setup window
    def setup_window(self):
        self.setWindowTitle = self.title
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
    
    # Setup layout
    def setup_layout(self):
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("window-central")
        
        self.central_layout = QHBoxLayout(self.central_widget)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        
    # Setup media
    def setup_media(self):
        pass
        
    # Setup content
    def setup_content(self):
        window_content = QWidget(self)
        window_content.setObjectName("window-content")
        
        content_layout = QVBoxLayout(window_content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        
        content_Tools = Tools(window_content)
        content_layout.addWidget(content_Tools)
        
        content_scroll = QScrollArea(window_content)
        content_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        content_scroll.setContentsMargins(0, 0, 0, 0)
        content_scroll.setWidgetResizable(True)
        
        content_items = QWidget(content_scroll)
        content_items.setObjectName("window-items")
        
        items_layout = QVBoxLayout(content_items)
        items_layout.setContentsMargins(0, 0, 0, 0)
        
        # for
        for key in self.data:
            data_item = QFrame(content_items)
            data_item.setObjectName("window-item")
            
            item_layout = QHBoxLayout(data_item)
            item_layout.setContentsMargins(0, 0, 0, 0)
            
            item_name = QLabel(str(key))
            item_name.setObjectName("window-name")
            item_layout.addWidget(item_name)
            
            item_input = QPlainTextEdit(data_item)
            item_input.insertPlainText(str(self.data[key]))
            item_layout.addWidget(item_input)
            
            data_item.setLayout(item_layout)
            items_layout.addWidget(data_item)

        content_scroll.setWidget(content_items)            
        content_layout.addWidget(content_scroll)
        window_content.setLayout(content_layout)
        self.central_layout.addWidget(window_content)
        
    # Get filename data
    def get_data(self):
        data = []
        
        with open(f"storage/json/{self.filename}.json") as file_json:
            data = json.load(file_json)
            
        for element in data:
            if element["name"] == str(self.name):
                self.data = element