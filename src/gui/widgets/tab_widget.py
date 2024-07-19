from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QTabWidget
from gui.widgets.equation_display import EquationDisplay
from gui.widgets.equation_input import EquationInput
from gui.widgets.graph import GraphWidget
from gui.widgets.table import TableWidget


class TabWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Layout principal das duas abas
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # Primeira aba - Método de Newton
        self.tab1 = QWidget()
        self.tab1_layout = QGridLayout(self.tab1)

        self.graph_widget = GraphWidget()
        self.table_widget = TableWidget()
        self.equation_input = EquationInput()
        self.equation_display = EquationDisplay(
            "f(x, y) = x^2 + y^2 - 1", "g(x, y) = x - y^2"
        )

        # Layout 1 do metodo de newton
        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.graph_widget)
        self.layout1.setContentsMargins(10, 10, 10, 10)  # Defina as margens
        self.layout1.setSpacing(10)  # Defina o espaçamento

        # Layout 2 do metodo de newton
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.table_widget)
        self.layout2.addWidget(self.equation_display)
        self.layout2.addWidget(self.equation_input)
        self.layout2.setContentsMargins(10, 10, 10, 10)  # Defina as margens
        self.layout2.setSpacing(10)  # Defina o espaçamento

        # Unindo os Layouts do metodo de newton em um
        self.tab1_layout.addLayout(self.layout1, 0, 0, 0, 4)
        self.tab1_layout.addLayout(self.layout2, 0, 5, 0, 2)

        self.tabs.addTab(self.tab1, "Método de Newton")

        # Segunda aba - backpropagation
        self.tab2 = QWidget()
        self.tab2_layout = QGridLayout(self.tab2)
        # Adicione aqui os widgets para a segunda aba
        self.tabs.addTab(self.tab2, "Backpropagation")
