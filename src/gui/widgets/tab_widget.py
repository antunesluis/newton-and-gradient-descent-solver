from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QTabWidget
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

        # Layout 1 do metodo de newton
        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.graph_widget)
        self.layout1.addWidget(self.equation_input)

        # Layout 2 do metodo de newton
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.table_widget)

        # Unindo os Layouts do metodo de newton em um
        self.tab1_layout.addLayout(self.layout1, 0, 0)
        self.tab1_layout.addLayout(self.layout2, 0, 3)

        self.tabs.addTab(self.tab1, "Método de Newton")

        # Segunda aba - backpropagation
        self.tab2 = QWidget()
        self.tab2_layout = QGridLayout(self.tab2)
        # Adicione aqui os widgets para a segunda aba
        self.tabs.addTab(self.tab2, "Backpropagation")
