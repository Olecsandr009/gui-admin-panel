from PyQt6.QtWidgets import QBoxLayout, QWidget
from PyQt6.QtCore import Qt

from abc import ABC, abstractmethod


class LayoutInterface(ABC):
    @abstractmethod
    def setLayoutMargins(self, left: int, top: int, right: int, bottom: int):
        pass

    @abstractmethod
    def setLayoutAlignment(self, alignment: Qt.AlignmentFlag):
        pass


class Layout(QBoxLayout, LayoutInterface):
    def __init__(self, direction: QBoxLayout.Direction, parent: QWidget = None):
        super().__init__(direction, parent)

    def setLayoutMargins(self, left: int, top: int, right: int, bottom: int):
        self.setContentsMargins(left, top, right, bottom)

    def setLayoutAlignment(self, alignment: Qt.AlignmentFlag):
        self.setAlignment(alignment)
