from PySide6.QtCore import Slot
from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QGridLayout
from gui.widgets.activation_button import ActivationButton
from gui.widgets.equation_input import EquationInput
from gui.widgets.graph import GraphWidget
from gui.widgets.table import TableWidget
from gui.widgets.result_display import ResultDisplay
from methods.equation_manager import EquationManager
from methods.backpropagation import CalculateBackpropagation


class BackpropagationTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.equationManager = EquationManager()
        self.setupUi()

    def setupUi(self):
        self.tabLayout = QGridLayout(self)

        self.graphWidget = GraphWidget()
        self.tableWidget = TableWidget()
        self.resultDisplay = ResultDisplay()
        self.equationInput = EquationInput("f(x, y)")
        self.xInitialInput = EquationInput("Initial x")
        self.yInitialInput = EquationInput("Initial y")
        self.activateButton = ActivationButton("Calcular")

        self.xInitialInput.returnPressed.connect(self.saveInitialValues)
        self.equationInput.returnPressed.connect(self.saveEquation)
        self.yInitialInput.returnPressed.connect(self.saveInitialValues)
        self.activateButton.clicked.connect(self.activateBackpropagation)

        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.graphWidget)

        self.initialValuesLayout = QHBoxLayout()
        self.initialValuesLayout.addWidget(self.xInitialInput)
        self.initialValuesLayout.addWidget(self.yInitialInput)
        self.initialValuesLayout.addWidget(self.activateButton)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.addWidget(self.tableWidget)
        self.rightLayout.addWidget(self.equationInput)
        self.rightLayout.addLayout(self.initialValuesLayout)
        self.rightLayout.addWidget(self.resultDisplay)
        self.rightLayout.setContentsMargins(20, 20, 50, 20)
        self.rightLayout.setSpacing(10)

        self.tabLayout.addLayout(self.leftLayout, 0, 0, 1, 3)
        self.tabLayout.addLayout(self.rightLayout, 0, 3, 1, 2)

    def saveEquation(self):
        print(f"Equation: {self.equationManager.equation1}")
        self.clearInitialValues()
        self.equationManager.setEquation1(self.equationInput.text())
        self.updateGraph()

    def saveInitialValues(self):
        x0 = self.xInitialInput.text()
        y0 = self.yInitialInput.text()
        print(f"Initial Values: x0 = {x0}, y0 = {y0}")

    def clearInitialValues(self):
        self.xInitialInput.clear()
        self.yInitialInput.clear()

    def updateGraph(self):
        self.resultDisplay.resetResults()
        f1 = self.equationManager.getLambdifiedFunction()
        if f1 is not None:
            self.graphWidget.plotContours(f1)
            return

        print(
            "Erro: Não foi possível atualizar o gráfico devido a uma equação inválida."
        )

    @Slot()
    def activateBackpropagation(self):
        equation = self.equationManager.equation1
        x0 = self.xInitialInput.text()
        y0 = self.yInitialInput.text()

        # Verificação de preenchimento dos campos
        if not (equation and x0 and y0):
            print("Erro: Preencha a equação e os valores iniciais.")
            return

        try:
            x0 = float(x0)
            y0 = float(y0)
        except ValueError:
            print("Erro: Os valores iniciais x0 e y0 devem ser números.")
            return

        f = self.equationManager.getLambdifiedFunction()
        if f is None:
            print(
                "Erro: Não foi possível lambdificar a equação. Verifique a equação de entrada."
            )
            return

        x_final, y_final, points = CalculateBackpropagation(equation, x0, y0)
        self.resultDisplay.updateResults(x_final, y_final)
        self.graphWidget.plotPoints(points)

        # Preenche a tabela com os dados da progressão
        data = []
        for n, (xn, yn) in enumerate(points):
            data.append([n, xn, yn])
        self.tableWidget.updateTable(data)
