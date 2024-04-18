from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon, QFont


class ButtonBorder():
    def __init__(self, parent, text, icon = None):
        super().__init__()
        
        self.parent = parent
        self.text = text
        self.icon = icon
        
    # Налаштування елементів
    def setup_layout(self):
        button_border = QPushButton(self.text, parent=self.parent)
        button_border.setObjectName("buttonBorder")
        
        font = self.setup_font()
        button_border.setFont(font)
        
        if self.icon:
            button_icon = QIcon(self.icon)
            button_border.setIcon(button_icon)
            
        return button_border
    
    # Налаштування фону
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        return font