from PySide6.QtCore import Slot
from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QGridLayout
from gui.widgets.activation_button import ActivationButton
from gui.widgets.equation_input import EquationInput
from gui.widgets.graph import GraphWidget
from gui.widgets.table import TableWidget
from gui.widgets.result_display import ResultDisplay
from methods.equation_manager import EquationManager
from methods.newton_method import CalculateNewtonMethod


class NewtonMethodTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.equation_manager = EquationManager()
        self.setupIu()

    def setupIu(self):
        self.tabLayout = QGridLayout(self)

        self.graphWidget = GraphWidget()
        self.tableWidget = TableWidget()
        self.resultDisplay = ResultDisplay()
        self.equationInput1 = EquationInput("f(x, y)")
        self.equationInput2 = EquationInput("g(x, y)")
        self.xInitial = EquationInput("Initial x")
        self.yInitial = EquationInput("Initial y")
        self.activateButton = ActivationButton("Calcular")

        self.equationInput1.returnPressed.connect(self.saveEquation1)
        self.equationInput2.returnPressed.connect(self.saveEquation2)
        self.xInitial.returnPressed.connect(self.saveInitialValues)
        self.yInitial.returnPressed.connect(self.saveInitialValues)
        self.activateButton.clicked.connect(self.activateNewtonMethod)

        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.graphWidget)

        self.initialValuesLayout = QHBoxLayout()
        self.initialValuesLayout.addWidget(self.xInitial)
        self.initialValuesLayout.addWidget(self.yInitial)
        self.initialValuesLayout.addWidget(self.activateButton)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.addWidget(self.tableWidget)
        self.rightLayout.addWidget(self.equationInput1)
        self.rightLayout.addWidget(self.equationInput2)
        self.rightLayout.addLayout(self.initialValuesLayout)
        self.rightLayout.addWidget(self.resultDisplay)
        self.rightLayout.setContentsMargins(20, 20, 50, 20)
        self.rightLayout.setSpacing(10)

        self.tabLayout.addLayout(self.leftLayout, 0, 0, 1, 3)
        self.tabLayout.addLayout(self.rightLayout, 0, 3, 1, 2)

    def saveEquation1(self):
        print(f"Equation 1: {self.equation_manager.equation1}")
        self.clearInitialValues()
        self.equation_manager.setEquation1(self.equationInput1.text())
        self.updateGraph()

    def saveEquation2(self):
        print(f"Equation 2: {self.equation_manager.equation2}")
        self.clearInitialValues()
        self.equation_manager.setEquation2(self.equationInput2.text())
        self.updateGraph()

    def saveInitialValues(self):
        x0 = self.xInitial.text()
        y0 = self.yInitial.text()
        print(f"Initial Values: x0 = {x0}, y0 = {y0}")

    def clearInitialValues(self):
        self.xInitial.clear()
        self.yInitial.clear()

    def updateGraph(self):
        self.resultDisplay.resetResults()
        f1, f2 = self.equation_manager.getLambdifiedFunctions()
        if f1 is not None:
            self.graphWidget.plot2DFunctions(f1, f2)
            return

        print(
            "Erro: Não foi possível atualizar o gráfico devido a uma equação inválida."
        )

    @Slot()
    def activateNewtonMethod(self):
        equation1 = self.equation_manager.equation1
        equation2 = self.equation_manager.equation2
        x0 = self.xInitial.text()
        y0 = self.yInitial.text()

        # Verificação de preenchimento dos campos
        if not (equation1 and equation2 and x0 and y0):
            print("Erro: Preencha todas as equações e valores iniciais.")
            return

        try:
            x0 = float(x0)
            y0 = float(y0)
        except ValueError:
            print("Erro: Os valores iniciais x0 e y0 devem ser números.")
            return

        f1, f2 = self.equation_manager.getLambdifiedFunctions()
        if f1 is None or f2 is None:
            print(
                "Erro: Não foi possível lambdificar as equações. Verifique as equações de entrada."
            )
            return

        x_final, y_final, points = CalculateNewtonMethod(equation1, equation2, x0, y0)
        self.resultDisplay.updateResults(x_final, y_final)
        self.graphWidget.plotPoints(points)

        # Preencher a tabela com os dados da progressão
        data = []
        for n, (xn, yn) in enumerate(points):
            data.append([n, xn, yn, f1(xn, yn), f2(xn, yn)])
        self.tableWidget.updateTable(data)
