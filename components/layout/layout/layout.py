from PyQt6.QtWidgets import QBoxLayout, QWidget
from PyQt6.QtCore import Qt

from abc import ABC, abstractmethod


class LayoutInterface:
    @abstractmethod
    def setLayoutMargins(self, left: int, top: int, right: int, bottom: int) -> None:
        pass

    @abstractmethod
    def setLayoutAlignment(self, alignment: Qt.AlignmentFlag) -> None:
        pass

    @abstractmethod
    def addLayoutWidget(self, widget: QWidget) -> None:
        pass

    @abstractmethod
    def addLayoutSpacing(self, space: int) -> None:
        pass


class Layout(QBoxLayout):
    def __init__(self, direction: QBoxLayout.Direction, parent: QWidget = None):
        super().__init__(direction, parent)

    # def setLayoutMargins(self, left: int, top: int, right: int, bottom: int):
    #     self.setContentsMargins(left, top, right, bottom)
    #
    # def setLayoutAlignment(self, alignment: Qt.AlignmentFlag):
    #     self.setAlignment(alignment)
    #
    # def addLayoutSpacing(self, space: int) -> None:
    #     self.addSpacing(space)
    #
    # def addLayoutWidget(self, widget: QWidget) -> None:
    #     self.addWidget(widget)
