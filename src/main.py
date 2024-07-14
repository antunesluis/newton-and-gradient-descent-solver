import sys

from PySide6.QtWidgets import QApplication
from gui.widgets.equation_input import EquationInput
from gui.widgets.main_window import MainWindow
from gui.widgets.graph import GraphWidget
from gui.widgets.table import TableWidget
from gui.widgets.styles import setupTheme

# Inicialização da aplicação
if __name__ == "__main__":
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Adicionar widgets à janela principal
    table_widget = TableWidget()
    graph_widget = GraphWidget()
    equation_input = EquationInput()

    window.addWidgetToGridLayout(graph_widget, 0, 0, 1, 2)

    window.addWidgetToGridLayout(table_widget, 0, 2, 1, 2)

    # Adicionar input para equação
    window.addWidgetToGridLayout(equation_input, 3, 0, 1, 1)

    window.show()
    sys.exit(app.exec())
