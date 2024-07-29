from PySide6.QtCore import Slot
from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QGridLayout
from gui.widgets.activation_button import ActivationButton
from gui.widgets.equation_input import EquationInput
from gui.widgets.graph import GraphWidget
from gui.widgets.message_box import MessageBox
from gui.widgets.table import TableWidget
from gui.widgets.result_display import ResultDisplay
from methods.equation_manager import EquationManager
from methods.newton_method import CalculateNewtonMethod
from utils.exceptions import CalculationError, InitialValuesError, InvalidEquationError


class NewtonMethodTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.equationManager = EquationManager()
        self.setupUI()

    def setupUI(self):
        """Configura a interface do usuário."""
        self.tabLayout = QGridLayout(self)

        self.graphWidget = GraphWidget()
        self.tableWidget = TableWidget()
        self.resultDisplay = ResultDisplay()
        self.equationInput1 = EquationInput("f(x, y)")
        self.equationInput2 = EquationInput("g(x, y)")
        self.xInitial = EquationInput("Initial x")
        self.yInitial = EquationInput("Initial y")
        self.activateButton = ActivationButton("Calcular")

        self.equationInput1.returnPressed.connect(self.saveEquations)
        self.equationInput2.returnPressed.connect(self.saveEquations)
        self.xInitial.returnPressed.connect(self.saveXInitialValue)
        self.yInitial.returnPressed.connect(self.saveYInitialValue)
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
            self.xInitial, self.equationManager.setXInitial, "xInitial"
        )

    @Slot()
    def saveYInitialValue(self):
        """Salva o valor inicial de y e o imprime no console."""
        self.validateAndSetInitialValue(
            self.yInitial, self.equationManager.setYInitial, "yInitial"
        )

    @Slot()
    def saveEquations(self):
        """Salva as equações fornecidas e atualiza o gráfico."""
        self.clearInitialValues()
        try:
            currentStrEq1 = self.equationInput1.text()
            currentStrEq2 = self.equationInput2.text()

            if currentStrEq1 != self.equationManager.strEquation1:
                self.equationManager.setStrEquation1(currentStrEq1)
                self.equationManager.setLambdifiedEquation1(currentStrEq1)

            if currentStrEq2 != self.equationManager.strEquation2:
                self.equationManager.setStrEquation2(currentStrEq2)
                self.equationManager.setLambdifiedEquation2(currentStrEq2)

            print(f"Equation 1: {currentStrEq1}")
            print(f"Equation 2: {currentStrEq2}")
            self.updateGraph()
        except InvalidEquationError as e:
            MessageBox.showErrorMessage(
                self, "Erro", f"Erro ao lambdificar equação: {str(e)}"
            )
        except Exception as e:
            MessageBox.showErrorMessage(self, "Erro inesperado", str(e))

    def clearInitialValues(self):
        """Limpa os valores iniciais dos campos de entrada."""
        self.xInitial.clear()
        self.yInitial.clear()

    def updateGraph(self):
        """Atualiza o gráfico com base nas funções lambdificadas."""
        self.resultDisplay.resetResults()
        try:
            lambdifiedFunc1 = self.equationManager.lambdifiedEquation1
            lambdifiedFunc2 = self.equationManager.lambdifiedEquation2
            if lambdifiedFunc1:
                self.graphWidget.plot2DFunctions(lambdifiedFunc1, lambdifiedFunc2)
        except Exception:
            MessageBox.showErrorMessage(
                self, "Erro", "Erro inesperado ao atualizar gráfico"
            )

    def validateInputs(self):
        """Valida se todos os campos obrigatórios estão preenchidos."""
        requiredFields = [
            self.equationManager.strEquation1,
            self.equationManager.strEquation2,
            self.equationManager.lambdifiedEquation1,
            self.equationManager.lambdifiedEquation2,
            self.equationManager.xInitial,
            self.equationManager.yInitial,
        ]
        if not all(requiredFields):
            MessageBox.showWarningMessage(
                self, "Inputs faltando", "Preencha todas as equações e valores iniciais"
            )
            return False
        return True

    def updateTable(self, points):
        """Atualiza a tabela com os dados da progressão."""
        lambdifiedEquation1 = self.equationManager.lambdifiedEquation1
        lambdifiedEquation2 = self.equationManager.lambdifiedEquation2

        if lambdifiedEquation1 and lambdifiedEquation2:
            data = [
                [n, xn, yn, lambdifiedEquation1(xn, yn), lambdifiedEquation2(xn, yn)]
                for n, (xn, yn) in enumerate(points)
            ]
            self.tableWidget.updateTable(data)

    @Slot()
    def activateNewtonMethod(self):
        """Ativa o método de Newton e atualiza a UI com os resultados."""
        if not self.validateInputs():
            return

        try:
            xFinal, yFinal, points = CalculateNewtonMethod(
                self.equationManager.strEquation1,
                self.equationManager.strEquation2,
                self.equationManager.xInitial,
                self.equationManager.yInitial,
            )
            self.resultDisplay.updateResults(xFinal, yFinal)
            self.graphWidget.plotPoints(points)
            self.updateTable(points)

        except CalculationError as e:
            MessageBox.showErrorMessage(
                self, "Erro", f"Erro ao realizar o cálculo do método: {str(e)}"
            )
        except Exception as e:
            MessageBox.showErrorMessage(self, "Erro inesperado", str(e))

