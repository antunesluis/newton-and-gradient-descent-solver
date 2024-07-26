from PySide6.QtCore import Slot
from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QGridLayout
from gui.widgets.activation_button import ActivationButton
from gui.widgets.equation_input import EquationInput
from gui.widgets.graph import GraphWidget
from gui.widgets.table import TableWidget
from gui.widgets.result_display import ResultDisplay
from methods.equation_manager import EquationManager
from methods.newton_method import calculate_newton_method


class NewtonMethodTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.equation_manager = EquationManager()

        self.tab1 = QWidget()
        self.tab1Layout = QGridLayout(self)

        self.graphWidget = GraphWidget()
        self.tableWidget = TableWidget()

        self.resultDisplay = ResultDisplay()
        self.equationInput1 = EquationInput("f(x, y)")
        self.equationInput2 = EquationInput("g(x, y)")
        self.xInitial = EquationInput("Initial x")
        self.yInitial = EquationInput("Initial y")

        self.equationInput1.returnPressed.connect(self.saveEquation1)
        self.equationInput2.returnPressed.connect(self.saveEquation2)
        self.xInitial.returnPressed.connect(self.saveInitialValues)
        self.yInitial.returnPressed.connect(self.saveInitialValues)

        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.graphWidget)
        self.layout2 = QVBoxLayout()

        self.layout2.addWidget(self.tableWidget)
        self.layout2.addWidget(self.equationInput1)
        self.layout2.addWidget(self.equationInput2)

        self.initialValuesLayout = QHBoxLayout()
        self.initialValuesLayout.addWidget(self.xInitial)
        self.initialValuesLayout.addWidget(self.yInitial)

        # Adicionando o botão de ativação
        self.activateButton = ActivationButton("Ativar")
        self.activateButton.clicked.connect(self.activateNewtonMethod)
        self.initialValuesLayout.addWidget(self.activateButton)

        self.layout2.addLayout(self.initialValuesLayout)

        self.layout2.addWidget(self.resultDisplay)
        self.layout2.setContentsMargins(20, 20, 50, 20)
        self.layout2.setSpacing(10)

        self.tab1Layout.addLayout(self.layout1, 0, 0, 1, 3)
        self.tab1Layout.addLayout(self.layout2, 0, 3, 1, 2)

    def saveEquation1(self):
        print(f"Equation 1: {self.equation_manager.equation1}")
        self.clearInitialValues()
        self.equation_manager.set_equation1(self.equationInput1.text())
        self.updateGraph()

    def saveEquation2(self):
        print(f"Equation 2: {self.equation_manager.equation2}")
        self.clearInitialValues()
        self.equation_manager.set_equation2(self.equationInput2.text())
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
        f1, f2 = self.equation_manager.get_lambdified_functions()
        if f1 is not None:
            self.graphWidget.plot(f1, f2)
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

        if equation1 and equation2 and x0 and y0:
            try:
                x0 = float(x0)
                y0 = float(y0)
                x_final, y_final, points = calculate_newton_method(
                    equation1, equation2, x0, y0
                )
                self.resultDisplay.updateResults(x_final, y_final)

                # Plotando novamente o gráfico para limpar os pontos anteriores
                self.graphWidget.plot_points(points)
            except ValueError:
                print("Erro: Os valores iniciais x0 e y0 devem ser números.")
        else:
            print("Erro: Preencha todas as equações e valores iniciais.")
