import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QWidget, QVBoxLayout


class GraphWidget(QWidget):
    def __init__(self, parent=None):
        plt.style.use("dark_background")

        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.figure, self.ax = plt.subplots(figsize=(10, 8))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.configStyle()

    def configStyle(self):
        self.ax.set_title("Graph of Equations")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        self.ax.grid(True)  # Add grid
        self.ax.set_aspect("equal", "box")
        self.figure.patch.set_linewidth(2)

        # Configura o fundo ao redor do gráfico como transparente
        self.figure.patch.set_alpha(0.0)  # Fundo da figura transparente

        # Configura a grade com opacidade
        self.ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)

        self.figure.tight_layout()
        self.ax.autoscale()

    def plot(self, f1, f2=None):
        self.clear()
        self.configStyle()  # Ensure styles are applied after clearing

        x = np.linspace(-10, 10, 400)
        y = np.linspace(-10, 10, 400)
        X, Y = np.meshgrid(x, y)

        Z1 = f1(X, Y)
        self.ax.contour(X, Y, Z1, levels=[0], colors="r", linestyles="solid")

        if f2 is not None:
            Z2 = f2(X, Y)
            self.ax.contour(X, Y, Z2, levels=[0], colors="b", linestyles="dashed")

        self.figure.tight_layout()
        self.canvas.draw()

    def plot_points(self, points):
        x_points, y_points = zip(*points)
        self.ax.plot(x_points, y_points, "go-")
        self.canvas.draw()

    def clear(self):
        self.ax.cla()
        self.figure.tight_layout()
