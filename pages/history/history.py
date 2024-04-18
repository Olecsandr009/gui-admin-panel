from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import os
from datetime import datetime

from pages.history.grid_layout.grid_layout import GridLayout
from components.buttons.button_border import ButtonBorder
from pages.history.title.title import Title


class History():
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        self.folder_path = "storage/json"
        self.files_list = self.get_files()
        
    # Налаштування елементів
    def setup_layout(self):
        history = QWidget(parent=self.parent)
        history_layout = QVBoxLayout(history)
        
        history_title = QWidget(parent=history)
        history_title.setFixedHeight(100)
        title_layout = QHBoxLayout(history_title)
        title_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        font = self.setup_font()
        
        title_text = QLabel("Історія", parent=history_title)
        title_text.setFont(font)
        
        title_button_frame = QFrame(parent=history_title)
        button_frame_layout = QHBoxLayout(title_button_frame)
        
        button_border = ButtonBorder(history_title, "Додати новий файл")
        history_button = button_border.setup_layout()
        button_frame_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        button_frame_layout.addWidget(history_button)
        
        title_text.setObjectName("historyTitle")
        
        title_text.setAlignment(Qt.AlignmentFlag.AlignLeft)

        title = Title(parent=history_title)
        
        title_layout.addWidget(title)
        title_layout.addWidget(title_text)
        title_layout.addWidget(title_button_frame)
        
        grid_frame = QFrame(parent=self.parent)
        frame_layout = QVBoxLayout(grid_frame)
        frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        grid_title = GridLayout(self.parent).show_item({
            "file_id": "№",
            "file_name": "Ім'я:",
            "last_change": "Остання зміна:",
            "file_size": "Розмір:",
            "file_type": "Тип:"
        }, title=True)
        grid_title.setObjectName("historyItemTitle")
        
        frame_layout.addWidget(grid_title)
        
        for index, file_data in enumerate(self.files_list):
            grid_layout = GridLayout(self.parent).show_item({
                "file_id": f"{index + 1}",
                "file_type": "json",
                **file_data
            })
            
            grid_layout.setObjectName("historyItem")
            
            frame_layout.addWidget(grid_layout)
            
        history_layout.addWidget(history_title)
        history_layout.addWidget(grid_frame)
            
        return history
    
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
    
    # Конвертация байтов
    def convert_bytes(self, bytes:int):
        pass