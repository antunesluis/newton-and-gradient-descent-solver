from PySide6.QtWidgets import (
    QMainWindow,
    QGridLayout,
    QWidget,
    QMessageBox,
    QLineEdit,
    QLabel,
)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()
        self.gridLayout = QGridLayout()
        self.cw.setLayout(self.gridLayout)
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle("Calculadora")

        # Adicionar label e input para equação
        self.equation_label = QLabel("Equação:")
        self.equation_input = QLineEdit()

        self.gridLayout.addWidget(self.equation_label, 1, 0)
        self.gridLayout.addWidget(self.equation_input, 2, 0)

    def AdjustFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToGridLayout(
        self,
        widget: QWidget,
        row: int,
        column: int,
        rowSpan: int = 1,
        columnSpan: int = 1,
    ):
        self.gridLayout.addWidget(widget, row, column, rowSpan, columnSpan)

    def makeMsgBox(self):
        return QMessageBox(self)

