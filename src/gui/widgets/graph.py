import pyqtgraph as pg
import numpy as np
from PySide6.QtWidgets import QWidget, QVBoxLayout


class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)  # type: ignore

        # Gerar dados aleatórios
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Adicionar uma curva ao gráfico
        self.plot_widget.plot(x, y, pen="r", label="Seno")

        # Adicionar uma legenda
        self.plot_widget.addLegend()

