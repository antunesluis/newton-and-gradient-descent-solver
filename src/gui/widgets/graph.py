import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QWidget, QVBoxLayout

from variables import XY_RANGE


class GraphWidget(QWidget):
    def __init__(self, parent=None):
        plt.style.use("dark_background")

        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.figure, self.ax = plt.subplots(figsize=(10, 8))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.ax.grid(True)  # Add grid
        self.configureStyle()

    def configureStyle(self):
        self.ax.set_title("Graph of Equations")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        self.ax.set_aspect("equal", "box")
        self.figure.patch.set_linewidth(2)

        # Configure the background around the graph as transparent
        self.figure.patch.set_alpha(0.0)  # Transparent figure background

        # Configure the grid with opacity
        self.ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)

        self.figure.tight_layout()
        self.ax.autoscale()

    def plot2DFunctions(self, func1, func2=None):
        self.clear()
        self.configureStyle()

        x = np.linspace(XY_RANGE[0], XY_RANGE[1], 400)
        y = np.linspace(XY_RANGE[0], XY_RANGE[1], 400)

        X, Y = np.meshgrid(x, y)

        Z1 = func1(X, Y)
        self.ax.contour(X, Y, Z1, levels=[0], colors="r", linestyles="solid")

        if func2 is not None:
            Z2 = func2(X, Y)
            self.ax.contour(X, Y, Z2, levels=[0], colors="b", linestyles="dashed")

        self.figure.tight_layout()
        self.canvas.draw()

    def plotContours(self, func, levels=10):
        self.clear()
        self.configureStyle()

        x = np.linspace(XY_RANGE[0], XY_RANGE[1], 400)
        y = np.linspace(XY_RANGE[0], XY_RANGE[1], 400)
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)

        contour = self.ax.contour(X, Y, Z, levels=levels, colors="white")
        self.ax.clabel(contour, inline=True, fontsize=8, fmt="%1.1f")
        self.canvas.draw()

    def plotPoints(self, points):
        """Plot points on the graph."""
        xPoints, yPoints = zip(*points)
        self.ax.plot(
            xPoints,
            yPoints,
            "go-",
            marker="o",
            linestyle="-",
            # markersize=5,
            # markeredgewidth=0.5,
        )
        self.canvas.draw()

    def clear(self):
        self.ax.cla()
        self.figure.tight_layout()
