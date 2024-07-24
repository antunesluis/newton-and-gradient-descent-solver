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

    def plot(self, x, y, z1, z2):
        self.plot_widget.clear()

        # Adicionar duas curvas ao gráfico
        self.plot_widget.plot(x.flatten(), z1.flatten(), pen="r", label="Equação 1")
        self.plot_widget.plot(x.flatten(), z2.flatten(), pen="b", label="Equação 2")

        # Adicionar uma legenda
        self.plot_widget.addLegend()

