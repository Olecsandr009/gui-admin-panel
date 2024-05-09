from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QFrame, QStackedWidget, QVBoxLayout, QLabel, QPlainTextEdit, QScrollArea, QInputDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap

from utils.windows.item.content.tools.tools import Tools
from utils.windows.item.content.content import Content
from utils.image.image import Image
from utils.scroll.scroll import Scroll
from components.ui.inputs.line_edit.line_edit import LineEdit
from components.ui.inputs.text_edit.text_edit import TextEdit
from components.ui.inputs.color_edit.color_edit import ColorEdit
from components.ui.inputs.urls_edit.urls_edit import UrlsEdit

from typing import Optional
import json


class Window(QWidget):
    # Initialize window widget
    def __init__(self, filename = None, name = None, parent: Optional[QWidget] = None):
        super(Window, self).__init__(parent)
        
        # Set object name
        self.setObjectName("item_window")
        
        # Default window name
        self.title = "Item window"
        # Default window position
        self.top = 80
        self.left = 200
        # Default widow size
        self.width = 1200
        self.height = 800
        
        self.filename = filename
        self.name = name
        
        self.data = None
        
        self.__getData()
        
        self.__applyStyles()
        self.__setupWindow()
        self.__setupLayout()
        self.__configureMedia()
        self.__configureContent()
        
        self.setLayout(self.window_layout)
        
    # Setup the window
    def __setupWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
    
    # Setup the window layout
    def __setupLayout(self):
        self.window_layout = QHBoxLayout(self)
        self.window_layout.setContentsMargins(0, 0, 0, 0)
        
    # Configure the window media
    def __configureMedia(self):
        window_media = QStackedWidget(self)
        window_media.setContentsMargins(0, 0, 0, 0)
        
        for image_url in self.data["images"]:
            image = Image("", 100, 100, self, str(image_url))
            image.setAlignment(Qt.AlignmentFlag.AlignCenter)
            window_media.addWidget(image)
        
        self.window_layout.addWidget(window_media)
        
    # Configure the window content
    def __configureContent(self):
        content_layout = Content(self)
                
        content_items = QWidget(content_layout)
        content_items.setObjectName("item_data_content")
        
        items_layout = QVBoxLayout(content_items)
        items_layout.setContentsMargins(0, 0, 0, 0)
        
        line_edit = LineEdit(content_items)
        line_edit.setFixedHeight(30)
        line_edit.setPlaceholderText("Test placeholder")
        items_layout.addWidget(line_edit)

        text_edit = TextEdit(self.data, "about", content_items)
        text_edit.setFixedHeight(30)
        # text_edit.setPlaceholderText("Test placeholder")
        text_edit.setText(" aldkfk asdfjasdlfadla fad slf lsdafj alsdf as;ld fasdl; fj")
        items_layout.addWidget(text_edit)

        color_edit = ColorEdit(content_items)
        color_edit.setFixedHeight(30)
        color_edit.setColor("#ffffff")
        color_edit.setColor("#443534")
        items_layout.addWidget(color_edit)

        urls_edit = UrlsEdit(self.data["images"], content_items)
        items_layout.addWidget(urls_edit)

        # for
        for key in self.data:
            data_item = QFrame(content_items)
            data_item.setObjectName("window-item")
            
            item_layout = QHBoxLayout(data_item)
            item_layout.setContentsMargins(0, 0, 0, 0)
            
            item_name = QLabel(str(key))
            item_name.setObjectName("window-name")
            item_layout.addWidget(item_name)
            
            test_layout = QWidget(data_item)
            test_layout_layout = QVBoxLayout(test_layout)
            # test_layout_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            item_input = QInputDialog(test_layout)
            item_input.setObjectName("window-input")
            # item_input.insertPlainText(str(self.data[key]))
            # item_input.setMaximumBlockCount(1)
            test_layout_layout.addWidget(item_input)
            test_layout.setLayout(test_layout_layout)
            item_layout.addWidget(test_layout)
            data_item.setLayout(item_layout)
            items_layout.addWidget(data_item)

        content_layout.setContent(content_items)
        
        self.window_layout.addWidget(content_layout)
        
    # Get the filename data
    def __getData(self):
        print("get data")
        data = []
        
        with open(f"storage/json/{self.filename}.json") as file_json:
            data = json.load(file_json)
            
        for element in data:
            if element["name"] == str(self.name):
                self.data = element
            
    # Apply the styles
    def __applyStyles(self):
        with open("styles/styles.css", "r") as file:
            self.setStyleSheet(file.read())
    