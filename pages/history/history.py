from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QStyleOption, QStyle
from PyQt6.QtGui import QFont, QPainter, QPaintEvent
from PyQt6.QtCore import Qt
import os
from datetime import datetime

from pages.history.grid_layout.grid_layout import GridLayout
from components.layout.title.title import Title
from components.ui.buttons.button import ButtonStyle


class History(QWidget):
    def __init__(self, parent, stack):
        super(History, self).__init__(parent)
        self.setObjectName("history")
        
        self.folder_path = "storage/json"
        self.files_list = self.get_files()
        self.parent = parent
        self.stack = stack
        
        self.setup_layout()
        self.grid_layout()
        
        self.setLayout(self.history_layout)
        
    # Setup history layout
    def setup_layout(self):
        self.history_layout = QVBoxLayout(self)
        self.history_layout.setContentsMargins(0, 0, 0, 0)
        
    # Setup grid layout
    def grid_layout(self):
        grid_frame = QFrame(parent=self)
        grid_frame.setObjectName("gridFrame")
        
        grid_layout = QVBoxLayout(grid_frame)
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        
        title_layout = Title(self)
        
        title_layout.setTitleText("Історія", 32)
        title_layout.setFixedHeight(100)
        title_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        title_layout.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
        
        title_layout.setButton("Додати файл", ButtonStyle.BORDER)
        title_layout.setButtonAlignment(Qt.AlignmentFlag.AlignRight)
        title_layout.setContentsMargins(0, 0, 16, 0)
        
        self.history_layout.addWidget(title_layout)
        
        grid_title = GridLayout(self, {
            "file_id": "№",
            "file_name": "Ім'я:",
            "last_change": "Остання зміна:",
            "file_size": "Розмір:",
            "file_type": "Тип:"
        }, self.stack, title=True)
        
        grid_layout.addWidget(grid_title)
        
        for index, file_data in enumerate(self.files_list):
            grid_row = GridLayout(self, {
                "file_id": f"{index + 1}",
                "file_type": "json",
                **file_data
            }, self.stack)
            
            grid_layout.addWidget(grid_row)
            
        self.history_layout.addWidget(grid_frame)
    
    # Налаштування фону
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(32)
        return font
    
    # Отримання файлів
    def get_files(self):
        files = os.listdir(self.folder_path)
        files_list = []
        
        if len(files):
            for file_name in files:
                file_data = {}
                
                file_path = f"{self.folder_path}/{file_name}"
                file_size = os.path.getsize(file_path)
                last_change = os.stat(file_path).st_mtime
                last_change_date = datetime.fromtimestamp(last_change)
                
                file_data["file_name"] = file_name.rstrip(".json")
                file_data['file_size'] = str(file_size)
                file_data["last_change"] = last_change_date.strftime("%Y-%m-%d")
                
                print(file_size)
                
                files_list.append(file_data)
                
        return files_list
    
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
    
    # Конвертация байтов
    def convert_bytes(self, bytes:int):
        pass