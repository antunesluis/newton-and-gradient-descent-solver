import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
import pyqtgraph as pg
from pyqtgraph.Qt.QtWidgets import QPushButton
from gui.widgets.styles import setupTheme


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo PyQtGraph com PySide6")

        # Criar um widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Botao genérico
        botao = QPushButton("dsadksa")

        # Layout vertical
        layout = QGridLayout(central_widget)

        # Criar um widget de gráfico
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget, 1, 1, 5, 5)  # type: ignore
        layout.addWidget(botao, 6, 2)  # type: ignore

        # Gerar dados
        x = np.linspace(0, 10, 100)
        y = np.cosh(x)  # Função seno

        # Adicionar uma curva ao gráfico
        self.plot_widget.plot(x, y, pen="r", label="Seno")

        # Adicionar uma legenda
        self.plot_widget.addLegend()


# Inicialização da aplicação
if __name__ == "__main__":
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Executa tudo
    window.show()
    app.exec()
