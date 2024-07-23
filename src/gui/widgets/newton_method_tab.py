from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from gui.widgets.equation_input import EquationInput
from gui.widgets.graph import GraphWidget
from gui.widgets.table import TableWidget
from gui.widgets.result_display import ResultDisplay


class NewtonMethodTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.tab1Layout = QGridLayout(self)

        self.graphWidget = GraphWidget()
        self.tableWidget = TableWidget()
        self.equationInput1 = EquationInput()
        self.equationInput2 = EquationInput()
        self.resultDisplay = ResultDisplay()

        # Layout 1 do metodo de newton
        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.graphWidget)
        self.layout1.setContentsMargins(10, 10, 10, 10)  # Defina as margens
        self.layout1.setSpacing(10)  # Defina o espaçamento

        # Layout 2 do metodo de newton
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.tableWidget)
        self.layout2.addWidget(self.resultDisplay)
        self.layout2.addWidget(self.equationInput1)
        self.layout2.addWidget(self.equationInput2)
        self.layout2.setContentsMargins(20, 20, 20, 20)  # Defina as margens
        self.layout2.setSpacing(10)  # Defina o espaçamento

        # Unindo os Layouts do metodo de newton em um
        self.tab1Layout.addLayout(self.layout1, 0, 0, 0, 4)
        self.tab1Layout.addLayout(self.layout2, 0, 5, 0, 2)
