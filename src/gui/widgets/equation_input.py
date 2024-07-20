from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from gui.widgets.equation_display import EquationDisplay
from variables import BIG_FONT_SIZE, MINIMUM_WIDHT, TEXT_MARGIN


class EquationInput(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        self.setPlaceholderText("Digite a equação...")
        self.textChanged.connect(self.onTextChanged)

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px;")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDHT)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setTextMargins(*margins)

    def onTextChanged(self):
        self.textChanged.emit(self.text())  # Emite o sinal com o texto atual
