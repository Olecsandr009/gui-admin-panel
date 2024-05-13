from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStyleOption, QStyle
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional

from utils.windows.item.content import Data, Apply
from utils.scroll.scroll import Scroll
from components.ui import Button
from components.layout import Tools, Container

from components.ui import Inputs


class Content(Container):
    # Initialize content widget
    def __init__(self, scheme, data, parent: Optional[QWidget] = None) -> None:
        super(Content, self).__init__()
        
        # Set the object name
        self.setObjectName("item_content")

        # Set the parent value
        self.parent = parent

        self.scheme = scheme
        self.data = data
        
        self.__contentLayout()
        self.__configureTools()
        self.__configureData()
        self.__configureApply()
        
    # Set the data content
    # def setContent(self, content: QWidget):
    #     self.content_data.setContent(content)

    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
        
    # Setup content layout
    def __contentLayout(self):
        self.addLayout(Container.Direction.TopToBottom)

    # Configure content tools
    def __configureTools(self):
        content_tools = Tools(self.parent)

        self.layout.addWidget(content_tools)
    
    def __configureData(self):
        self.content_data = Data(self)
        self.content_data.setContentsMargins(0, 16, 32, 16)

        self.content_data.setInputsScheme(self.scheme, self.data)
        
        self.layout.addWidget(self.content_data)
    
    def __configureApply(self):
        content_apply = Apply(self)
        content_apply.setAlignment(Qt.AlignmentFlag.AlignRight)
        content_apply.setContentsMargins(0, 0, 32, 32)
        
        content_apply.setButtonLayout("Відміна", Button.ButtonStyle.BORDER)
        content_apply.setButtonLayout("Зберегти", Button.ButtonStyle.FILL)
        
        self.layout.addWidget(content_apply)