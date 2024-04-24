from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QStackedWidget, QFrame, QHBoxLayout, QStyleOption, QStyle
from PyQt6.QtGui import QFont, QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import List, Optional

from components.sidebar.logo.logo import Logo
from utils.stacked_nav.stacked_nav import StackedNav


class Sidebar(QWidget):
    def __init__(
        self,
        stack: QStackedWidget,
        list: List[str],
        parent: Optional[QWidget]
    ):
        # Sidebar layout
        super(Sidebar, self).__init__(parent)
        self.setObjectName("sidebar")
        
        self.setFixedWidth(250)

        self.parent = parent
        self.stack = stack
        self.list = list
        
        self.setup_layout()
        self.logo_layout()
        self.nav_layout()
        
        self.setLayout(self.sidebar_layout)
        
    # Setup sidebar layout
    def setup_layout(self):
        self.sidebar_layout = QVBoxLayout(self)
        self.sidebar_layout.setContentsMargins(12, 12, 12, 12)
        self.sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
    # Setup logo layout
    def logo_layout(self):
        logo = Logo(self)
        self.sidebar_layout.addWidget(logo)
        self.sidebar_layout.addSpacing(20)
        
    # Setup navigation layout
    def nav_layout(self):
        self.sidebar_nav = QFrame(self)
        self.sidebar_nav.setObjectName("sidebar_nav")
        
        nav_layout = QVBoxLayout(self.sidebar_nav)
        nav_layout.setContentsMargins(0,0,0,0)
        
        self.fill_navigation_list(layout=nav_layout, list=self.list)
        
        self.sidebar_layout.addWidget(self.sidebar_nav)
        self.sidebar_layout.addSpacing(20)
        
    # Setup font
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        return font
    
    # Заповнення списку для навігації
    def fill_navigation_list(self, layout: QVBoxLayout | QHBoxLayout, list: List[str]):
        if not len(list): return
        
        for index, item in enumerate(list):
            button = QPushButton(item)
            button.setObjectName("ItemBtn")
            button.setFont(self.setup_font())
            
            if index == 0:
                button.setStyleSheet("QPushButton {background-color: #191919}")
            
            layout.addWidget(button)
            
            def on_button_click(clicked_index=index):
                return lambda: self.showPage(index=clicked_index)
            
            button.clicked.connect(on_button_click())
            
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
                
    # Відобраєення певної сторінки  
    def showPage(self, index):
        self.stack.setCurrentIndex(index)

        for button in self.sidebar_nav.findChildren(QPushButton):
            button_index = self.sidebar_nav.findChildren(QPushButton).index(button)
            button.setStyleSheet("QPushButton {background-color: transparent;}")
            
            if button_index == index:
                button.setStyleSheet("QPushButton {background-color: #191919}")