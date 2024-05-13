from components.layout import Frame
from utils.image.image import Image

from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtCore import Qt


class Media(Frame):
    # Initialize media
    def __init__(self, data, key: str):
        super().__init__()

        self.data = data
        self.key = key

        self.addLayout(Frame.Direction.TopToBottom)

        self.__configureMedia()

    # Configure the window media
    def __configureMedia(self):
        window_media = QStackedWidget(self)
        window_media.setContentsMargins(0, 0, 0, 0)

        for image_url in self.data[self.key]:
            image = Image("", 100, 100, self, str(image_url))
            image.setAlignment(Qt.AlignmentFlag.AlignCenter)
            window_media.addWidget(image)

        self.layout.addWidget(window_media)
