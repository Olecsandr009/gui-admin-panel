from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle, QVBoxLayout, QFrame, QHBoxLayout, QSlider, QLabel
from PyQt6.QtGui import QPainter, QPaintEvent, QPixmap, QMouseEvent, QColor
from PyQt6.QtCore import Qt

import numpy as np

from typing import Optional

from components.ui.buttons.button import Button
from components.ui.buttons.button import ButtonStyle


class Window(QWidget):
    # Initialize the apply widget
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(Window, self).__init__(parent)

        # Set the object name
        self.setObjectName("inputs_window")
        self.setAcceptDrops(True)

        self.color = QColor()

        # Default window name
        self.title = "Item window"
        # Default window position
        self.top = 200
        self.left = 300
        # Default widow size
        self.width = 300
        self.height = 400
        # Default color circle
        self.circle_width = 200
        self.circle_height = 200

        # Default margin values
        self.window_margin = [16, 16, 16, 16]
        self.container_margin = [16, 16, 16, 16]
        self.buttons_margin = [0, 0, 0, 0]

        self.__setupWindow()
        self.__applyStyles()
        self.__setupLayout()
        self.__configureContainer()
        # self.__configureColorPicker()
        self.__configureColorResult()
        self.__configureColorCircle()
        self.__configureColorSlider_1()
        self.__configureColorSlider_2()

        self.__configureColorButtons()
        self.__configureButtonClose()
        self.__configureButtonApply()

        self.setLayout(self.window_layout)

        self.sliderChangeEvent()
        self.setGradientSlider()

    # Set the margin values
    def setContentMargins(self, left: int, top: int, right: int, bottom: int):
        self.window_layout.setContentsMargins(left, top, right, bottom)

    # Set the container margin values
    def setContainerContentMargins(self, left: int, top: int, right: int, bottom: int):
        self.container_layout.setContentsMargins(left, top, right, bottom)

    # Set the alignment value
    def setAlignment(self, alignment: Qt.AlignmentFlag):
        self.window_layout.setAlignment(alignment)

    # Set the container alignment value
    def setContainerAlignment(self, alignment: Qt.AlignmentFlag):
        self.container_layout.setAlignment(alignment)

    # The mouse event handler to the get pixel
    def _getPixel(self, event: QMouseEvent):
        x = event.pos().x()
        y = event.pos().y()
        c = self.image.toImage().pixel(x, y)  # color code (integer) 3235912

        self.color.setRgba(c)  # color object
        self.setGradientSlider()
        self.sliderChangeEvent(event=event)

    # The click event handler to the close
    def _closeClickHandler(self):
        self.close()

    # The click event handler to the apply
    def _applyClickHandler(self):
        self.close()

    # Set the gradient slider
    def setGradientSlider(self):
        self.color_slider_2.setStyleSheet(f'''QSlider::groove:horizontal {{
                                                    background:qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                                    stop:0 #fff, stop:1 {self.color.name()},);
                                                }}
                                                ''')

    # Set the event handler the of slider change
    def sliderChangeEvent(self, event=None):
        self.color.setHsv(self.color.getHsv()[0], self.color_slider_2.value(), self.color_slider_1.value())
        self.color_result.setText(self.color.name().upper())
        text_color = QColor()
        if np.sum(self.color.getRgb()) > 470:
            text_color.setNamedColor('#000')
        else:
            text_color.setNamedColor('#fff')

        self.color_result.setStyleSheet(
            f'#inputs_window_color_result {{background-color:{self.color.name()}; color: {text_color.name()}}};'
        )

    # Setup the window
    def __setupWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)

    # Apply the styles
    def __applyStyles(self):
        with open("styles/styles.css", "r") as file:
            self.setStyleSheet(file.read())

    # Setup the widget layout
    def __setupLayout(self):
        self.window_layout = QVBoxLayout(self)
        self.window_layout.setContentsMargins(*self.window_margin)

    # Configure the widget container
    def __configureContainer(self):
        self.window_container = QFrame(self)
        self.window_container.setObjectName("inputs_window_color_edit_container")

        self.container_layout = QVBoxLayout(self.window_container)
        self.container_layout.setContentsMargins(*self.container_margin)

        self.window_layout.addWidget(self.window_container)

    # Configure the color result
    def __configureColorResult(self):
        self.color_result = QLabel(self.window_container)
        self.color_result.setObjectName("inputs_window_color_result")
        self.color_result.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.color_result.setFixedHeight(30)

        self.setStyleSheet("#inputs_window_color_result {color: #E1E1E1}")

        self.container_layout.addWidget(self.color_result)
        self.container_layout.addSpacing(16)

    # Configure the color circle
    def __configureColorCircle(self):
        self.color_circle = QLabel(self.window_container)
        self.color_circle.setObjectName("inputs_window_color_circle")
        self.color_circle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.image = QPixmap('media/color_picker/color_wheel.png')
        self.color_circle.setPixmap(self.image.scaled(self.circle_width, self.circle_height))
        self.color_circle.mousePressEvent = self._getPixel

        self.container_layout.addWidget(self.color_circle)
        self.container_layout.addSpacing(16)

    # Configure the color slider
    def __configureColorSlider_1(self):
        self.color_slider_1 = QSlider(self.window_container)
        self.color_slider_1.setObjectName("inputs_window_color_slider_1")
        self.color_slider_1.setMaximum(255)
        self.color_slider_1.setProperty("value", 255)
        self.color_slider_1.setOrientation(Qt.Orientation.Horizontal)

        self.color_slider_1.valueChanged.connect(self.sliderChangeEvent)

        self.container_layout.addWidget(self.color_slider_1)
        self.container_layout.addSpacing(16)

    def __configureColorSlider_2(self):
        self.color_slider_2 = QSlider(self.window_container)
        self.color_slider_2.setObjectName("inputs_window_color_slider_2")
        self.color_slider_2.setMaximum(255)
        self.color_slider_2.setProperty("value", 255)
        self.color_slider_2.setOrientation(Qt.Orientation.Horizontal)

        self.color_slider_2.valueChanged.connect(self.sliderChangeEvent)

        self.container_layout.addWidget(self.color_slider_2)
        self.container_layout.addSpacing(16)

    # Configure the color buttons bottom
    def __configureColorButtons(self):
        self.buttons_bottom = QWidget(self.window_container)
        self.buttons_bottom.setObjectName("inputs_window_color_buttons")

        self.buttons_layout = QHBoxLayout(self.buttons_bottom)
        self.buttons_layout.setContentsMargins(*self.buttons_margin)
        self.buttons_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.buttons_bottom.setLayout(self.buttons_layout)

        self.container_layout.addWidget(self.buttons_bottom)

    # Configure the close button
    def __configureButtonClose(self):
        self.button_close = Button(self.buttons_bottom)
        self.button_close.setButtonLayout("Відмінити", ButtonStyle.BORDER)
        self.button_close.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.button_close.clicked(self._closeClickHandler)

        self.buttons_layout.addWidget(self.button_close)

    # Configure the apply button
    def __configureButtonApply(self):
        self.button_apply = Button(self.buttons_bottom)
        self.button_apply.setButtonLayout("Зберегти", ButtonStyle.FILL)
        self.button_apply.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.button_apply.clicked(self._applyClickHandler)

        self.buttons_layout.addWidget(self.button_apply)
