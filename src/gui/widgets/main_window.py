from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from gui.widgets.tab_widget import TabWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Calculadora com Abas")

        self.cw = QWidget()
        self.layout = QVBoxLayout(self.cw)  # type: ignore
        self.setCentralWidget(self.cw)

        self.tab_widget = TabWidget(self)
        self.layout.addWidget(self.tab_widget)  # type: ignore
