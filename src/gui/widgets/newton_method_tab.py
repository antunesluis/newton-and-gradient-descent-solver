from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from gui.widgets.equation_input import EquationInput
from gui.widgets.graph import GraphWidget
from gui.widgets.table import TableWidget
from gui.widgets.result_display import ResultDisplay

import numpy as np
import sympy as sp


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

        self.equationInput1.returnPressed.connect(self.saveEquation1)
        self.equationInput2.returnPressed.connect(self.saveEquation2)

        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.graphWidget)
        self.layout1.setContentsMargins(10, 10, 10, 10)
        self.layout1.setSpacing(10)

        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.tableWidget)
        self.layout2.addWidget(self.equationInput1)
        self.layout2.addWidget(self.equationInput2)
        self.layout2.addWidget(self.resultDisplay)
        self.layout2.setContentsMargins(20, 20, 20, 20)
        self.layout2.setSpacing(10)

        self.tab1Layout.addLayout(self.layout1, 0, 0, 1, 3)
        self.tab1Layout.addLayout(self.layout2, 0, 3, 1, 2)

    def saveEquation1(self):
        self.equation1 = self.equationInput1.text()
        print(f"Equation 1: {self.equation1}")
        self.updateGraph()

    def saveEquation2(self):
        self.equation2 = self.equationInput2.text()
        print(f"Equation 2: {self.equation2}")
        self.updateGraph()

    def updateGraph(self):
        if self.equation1:
            try:
                x_sym, y_sym = sp.symbols("x y")
                eq1_sym = sp.sympify(self.equation1.replace("^", "**"))

                f1 = sp.lambdify((x_sym, y_sym), eq1_sym, "numpy")

                if self.equation2:
                    eq2_sym = sp.sympify(self.equation2.replace("^", "**"))
                    f2 = sp.lambdify((x_sym, y_sym), eq2_sym, "numpy")
                    self.graphWidget.plot(f1, f2)
                else:
                    self.graphWidget.plot(f1)

            except Exception as e:
                print(f"Erro ao avaliar equações: {e}")
