from PyQt6.QtGui import QFont

import os
from dotenv import load_dotenv

load_dotenv()


class Font(QFont):
    # Initialize font
    def __init__(self) -> None:
        super(Font, self).__init__()
        
        # Default the font family
        self.font_family = os.getenv("FONT_FAMILY")
        # Default the font size
        self.font_size = os.getenv("FONT_SIZE")
        # Default the font weight
        self.font_weight = os.getenv("FONT_REGULAR")
        
        self.__configureFont()
        
    # Set the font family
    def setFamily(self, family: str | None) -> None:
        return super().setFamily(family)
        
    # Set the font size value
    def setPointSize(self, size: int) -> None:
        return super().setPointSize(size)
    
    # Set the font weight value
    def setWeight(self, weight: int) -> None:
        return super().setWeight(weight)
    
    # Configure the text font
    def __configureFont(self) -> None:
        self.setFamily(str(self.font_family))
        self.setPointSize(int(self.font_size))
        self.setWeight(int(self.font_weight))