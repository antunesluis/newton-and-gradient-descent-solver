from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from variables import BIG_FONT_SIZE


class EquationDisplay(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fontSize = BIG_FONT_SIZE
        self.eq1 = QLabel()
        self.eq2 = QLabel()
        self.configStyle()

        layout = QVBoxLayout()
        layout.addWidget(self.eq1)
        layout.addWidget(self.eq2)

        self.setLayout(layout)

    def configStyle(self):
        font = self.font()
        font.setPointSize(24)
        self.setFont(font)
        self.eq1.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.eq1.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )

    def updateEquations(self, eq1_text, eq2_text):
        self.eq1.setText(eq1_text)
        self.eq2.setText(eq2_text)
