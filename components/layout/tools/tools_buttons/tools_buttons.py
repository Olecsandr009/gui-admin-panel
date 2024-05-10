from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QIcon, QPaintEvent, QPainter

from components.layout.frame.frame import Frame
from components.ui.buttons.button import Button, ButtonStyle


class ToolsButtons(Frame):
    # Initialize tools buttons
    def __init__(self, main: QWidget):
        super().__init__()

        self.main: QWidget = main

        self.addLayout(self.Direction.LeftToRight)

        self.__addShowButton()
        self.__addMaximizeButton()
        self.__addCloseButton()

    # Add show button
    def __addShowButton(self):
        icon = QIcon("media/icons/minus.png")

        button = Button(self)
        button.setButtonLayout("", ButtonStyle.DEFAULT)
        button.button.setIcon(icon)

        button.clicked(self.main.showMinimized)

        self.layout.addWidget(button)
        self.layout.addSpacing(6)

    # Add maximize button
    def __addMaximizeButton(self):
        button = Button(self)
        button.setButtonLayout("", ButtonStyle.DEFAULT)
        button.button.setIcon(self.__toggleMaximizedIcon())

        button.clicked(self.__toggleMaximized)

        self.layout.addWidget(button)
        self.layout.addSpacing(6)

    # Add close button
    def __addCloseButton(self):
        icon = QIcon("media/icons/close.png")

        button = Button(self)
        button.setButtonLayout("", ButtonStyle.DEFAULT)
        button.button.setIcon(icon)

        button.clicked(self.main.close)

        self.layout.addWidget(button)

    # Toggle icon
    def __toggleMaximizedIcon(self):
        if self.main.isMaximized():
            return QIcon("media/icons/minimize.png")
        else:
            return QIcon("media/icons/maximize.png")

    # Зміна стану вікна
    def __toggleMaximized(self):
        if self.main.isMaximized():
            self.main.showNormal()
        else:
            self.main.showMaximized()

    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
