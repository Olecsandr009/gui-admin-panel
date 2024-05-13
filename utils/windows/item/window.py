from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QLabel, QPlainTextEdit, QScrollArea, QInputDialog
from PyQt6.QtCore import Qt

from utils.windows.item import Content, Media
from utils.image.image import Image
from utils.scroll.scroll import Scroll

from enum import Enum

from components.layout import Container
from components.ui.inputs import LineEdit, TextEdit, ColorEdit, UrlsEdit, InputsScheme

import json


class Window(Container):

    InputsScheme = InputsScheme

    # Initialize window widget
    def __init__(self, filename=None, name=None):
        super(Window, self).__init__()

        # Content Scheme
        self.contentScheme = [
            {
                "key": "name",
                "input": InputsScheme.LineEdit
            },
            {
                "key": "about",
                "input": InputsScheme.TextEdit
            },
            {
                "key": "discount",
                "input": InputsScheme.LineEdit
            },
            {
                "key": "price",
                "input": InputsScheme.LineEdit
            },
            {
                "key": "article",
                "input": InputsScheme.LineEdit
            },
            {
                "key": "colors",
                "input": InputsScheme.ColorEdit
            },
            {
                "key": "memory",
                "input": InputsScheme.LineEdit
            },
            {
                "key": "likes",
                "input": InputsScheme.LineEdit
            }
        ]

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
        self.__configureMedia()
        self.__configureContent()
        
    # Setup the window
    def __setupWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.addLayout(Container.Direction.LeftToRight)

    # Configure the window media
    def __configureMedia(self):
        media = Media(self.data, "images")

        self.layout.addWidget(media)

    # Configure the window content
    def __configureContent(self):
        content_layout = Content(self.contentScheme, self.data, self)
                
        # content_items = QWidget(content_layout)
        # content_items.setObjectName("item_data_content")
        
        # items_layout = QVBoxLayout(content_items)
        # items_layout.setContentsMargins(0, 0, 0, 0)
        
        # line_edit = LineEdit(content_items)
        # line_edit.setFixedHeight(30)
        # line_edit.setPlaceholderText("Test placeholder")
        # items_layout.addWidget(line_edit)

        # text_edit = TextEdit(self.data, "about", content_items)
        # text_edit.setFixedHeight(30)
        # text_edit.setText(" aldkfk asdfjasdlfadla fad slf lsdafj alsdf as;ld fasdl; fj")
        # items_layout.addWidget(text_edit)

        # color_edit = ColorEdit(content_items)
        # color_edit.setFixedHeight(30)
        # color_edit.setColor("#ffffff")
        # color_edit.setColor("#443534")
        # items_layout.addWidget(color_edit)

        # urls_edit = UrlsEdit(self.data["images"], content_items)
        # items_layout.addWidget(urls_edit)

        # # for
        # for key in self.data:
        #     data_item = QFrame(content_items)
        #     data_item.setObjectName("window-item")
        #
        #     item_layout = QHBoxLayout(data_item)
        #     item_layout.setContentsMargins(0, 0, 0, 0)
        #
        #     item_name = QLabel(str(key))
        #     item_name.setObjectName("window-name")
        #     item_layout.addWidget(item_name)
        #
        #     test_layout = QWidget(data_item)
        #     test_layout_layout = QVBoxLayout(test_layout)
        #     # test_layout_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        #     item_input = QInputDialog(test_layout)
        #     item_input.setObjectName("window-input")
        #     # item_input.insertPlainText(str(self.data[key]))
        #     # item_input.setMaximumBlockCount(1)
        #     test_layout_layout.addWidget(item_input)
        #     test_layout.setLayout(test_layout_layout)
        #     item_layout.addWidget(test_layout)
        #     data_item.setLayout(item_layout)
        #     items_layout.addWidget(data_item)

        # content_layout.setContent(content_items)
        
        self.layout.addWidget(content_layout)
        
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
    