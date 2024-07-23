from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from variables import MEDIUM_FONT_SIZE


class ResultDisplay(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fontSize = MEDIUM_FONT_SIZE

        # Inicialize os valores de resultado com um texto padrão
        self.xResult = QLabel("X: --")
        self.yResult = QLabel("Y: --")
        self.configStyle()

        layout = QVBoxLayout()
        layout.addWidget(self.xResult)
        layout.addWidget(self.yResult)

        self.setLayout(layout)

    def configStyle(self):
        # Configure o estilo da fonte
        font = self.font()
        font.setPointSize(self.fontSize)

        # Configure o estilo dos labels
        self.xResult.setFont(font)
        self.yResult.setFont(font)

        self.xResult.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        self.yResult.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )

    def updateResults(self, x_value, y_value):
        # Atualize os textos dos labels com os valores encontrados
        self.xResult.setText(f"X: {x_value}")
        self.yResult.setText(f"Y: {y_value}")

