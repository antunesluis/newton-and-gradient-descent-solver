from PySide6.QtWidgets import QPushButton
from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, MINIMUM_WIDHT


class ActivationButton(QPushButton):
    def __init__(self, label, *args, **kwargs):
        super().__init__(label, *args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(BIG_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(MINIMUM_WIDHT, 60)
