from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from gui.widgets.equation_input import EquationInput
from gui.widgets.graph import GraphWidget
from gui.widgets.table import TableWidget
from gui.widgets.result_display import ResultDisplay


class NewtonMethodTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.tab1 = QWidget()
        self.tab1Layout = QGridLayout(self)

        self.graphWidget = GraphWidget()
        self.tableWidget = TableWidget()

        self.resultDisplay = ResultDisplay()
        self.equationInput1 = EquationInput("f(x, y)")
        self.equationInput2 = EquationInput("g(x, y)")

        self.equation1 = ""
        self.equation2 = ""

        self.equationInput1.equationChanged.connect(self.saveEquation1)
        self.equationInput2.equationChanged.connect(self.saveEquation2)

        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.graphWidget)
        self.layout1.setContentsMargins(10, 10, 10, 10)
        self.layout1.setSpacing(10)

        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.tableWidget)
        self.layout2.addWidget(self.equationInput1)
        self.layout2.addWidget(self.equationInput2)
        self.layout2.addWidget(self.resultDisplay)
        self.layout2.setContentsMargins(20, 20, 20, 20)  # Defina as margens
        self.layout2.setSpacing(10)  # Defina o espaçamento

        self.tab1Layout.addLayout(self.layout1, 0, 0, 0, 4)
        self.tab1Layout.addLayout(self.layout2, 0, 5, 0, 2)

    def saveEquation1(self, text):
        self.equation1 = text

    def saveEquation2(self, text):
        self.equation2 = text
