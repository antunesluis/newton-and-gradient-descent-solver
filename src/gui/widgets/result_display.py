from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from variables import MEDIUM_FONT_SIZE


class ResultDisplay(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fontSize = MEDIUM_FONT_SIZE

        self.xResult = QLabel("X: --")
        self.yResult = QLabel("Y: --")
        self.configStyle()

        layout = QVBoxLayout()
        layout.addWidget(self.xResult)
        layout.addWidget(self.yResult)

        self.setLayout(layout)

    def configStyle(self):
        font = self.font()
        font.setPointSize(self.fontSize)

        self.xResult.setFont(font)
        self.yResult.setFont(font)

        self.xResult.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        self.yResult.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )

    def updateResults(self, x_value, y_value):
        formatted_x_value = (
            f"{x_value:.4f}" if isinstance(x_value, (int, float)) else x_value
        )
        formatted_y_value = (
            f"{y_value:.4f}" if isinstance(y_value, (int, float)) else y_value
        )
        self.xResult.setText(f"X: {formatted_x_value}")
        self.yResult.setText(f"Y: {formatted_y_value}")

    def resetResults(self):
        self.updateResults("--", "--")
