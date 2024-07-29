from PySide6.QtCore import Slot
from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QGridLayout
from gui.widgets.activation_button import ActivationButton
from gui.widgets.equation_input import EquationInput
from gui.widgets.graph import GraphWidget
from gui.widgets.message_box import MessageBox
from gui.widgets.table import TableWidget
from gui.widgets.result_display import ResultDisplay
from methods.equation_manager import EquationManager
from methods.backpropagation import CalculateBackpropagation
from utils.exceptions import InitialValuesError, InvalidEquationError


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

        self.xInitialInput.returnPressed.connect(self.saveXInitialValue)
        self.yInitialInput.returnPressed.connect(self.saveYInitialValue)
        self.equationInput.returnPressed.connect(self.saveEquation)
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

    @Slot()
    def saveEquation(self):
        self.clearInitialValues()
        try:
            currentStrEq = self.equationInput.text()
            if currentStrEq != self.equationManager.strEquation1:
                self.equationManager.setStrEquation1(currentStrEq)
                self.equationManager.setLambdifiedEquation1(currentStrEq)

            print(f"Equation 1: {currentStrEq}")
            self.updateGraph()
        except InvalidEquationError as e:
            MessageBox.showErrorMessage(
                self, "Erro", f"Erro ao lambdificar equação: {str(e)}"
            )
        except Exception as e:
            MessageBox.showErrorMessage(self, "Erro inesperado", str(e))

    def validateAndSetInitialValue(self, value, setterFunc, valueName):
        try:
            valueText = value.text().strip()
            setterFunc(valueText)
            print(
                f"Initial Value {valueName} = {getattr(self.equationManager, valueName)}"
            )
        except InitialValuesError as e:
            MessageBox.showErrorMessage(
                self, "Erro", f"Erro ao receber valor inicial de {valueName}: {str(e)}"
            )
        except Exception as e:
            MessageBox.showErrorMessage(self, "Erro inesperado", str(e))

    @Slot()
    def saveXInitialValue(self):
        """Salva o valor inicial de x e o imprime no console."""
        self.validateAndSetInitialValue(
            self.xInitialInput, self.equationManager.setXInitial, "xInitial"
        )

    @Slot()
    def saveYInitialValue(self):
        """Salva o valor inicial de y e o imprime no console."""
        self.validateAndSetInitialValue(
            self.yInitialInput, self.equationManager.setYInitial, "yInitial"
        )

    def clearInitialValues(self):
        self.xInitialInput.clear()
        self.yInitialInput.clear()

    def updateGraph(self):
        self.resultDisplay.resetResults()
        try:
            lambdified_func1 = self.equationManager.lambdifiedEquation1
            if lambdified_func1 is not None:
                self.graphWidget.plotContours(lambdified_func1)
                return
        except Exception:
            MessageBox.showErrorMessage(
                self, "Erro", "Erro inesperado ao atualizar gráfico"
            )

    @Slot()
    def activateBackpropagation(self):
        equation = self.equationManager.strEquation1
        x0 = self.equationManager.xInitial
        y0 = self.equationManager.yInitial

        # Verificação de preenchimento dos campos
        if not (equation and x0 and y0):
            MessageBox.showWarningMessage(
                self, "Inputs faltando", "Preencha todas as equações e valores iniciais"
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
