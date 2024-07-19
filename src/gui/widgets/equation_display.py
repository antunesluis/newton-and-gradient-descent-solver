from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from variables import BIG_FONT_SIZE


class EquationDisplay(QWidget):
    def __init__(self, eq1, eq2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.eq1 = eq1
        self.eq2 = eq2
        self.configStyle()

    def configStyle(self):
        layout = QVBoxLayout()
        font_size = BIG_FONT_SIZE

        eq1_label = QLabel(self.eq1)
        eq2_label = QLabel(self.eq2)

        # Configurar o estilo das equações
        font = eq1_label.font()
        font.setPointSize(font_size)

        eq1_label.setFont(font)
        eq2_label.setFont(font)

        eq1_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        eq2_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )

        layout.addWidget(eq1_label)
        layout.addWidget(eq2_label)

        self.setLayout(layout)
