from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from gui.widgets.gradient_descent_tab import GradientDescentTab
from gui.widgets.newton_method_tab import NewtonMethodTab


class TabWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        tabMainLayout = QVBoxLayout()
        self.setLayout(tabMainLayout)

        self.tabs = QTabWidget()
        tabMainLayout.addWidget(self.tabs)

        # Primeira aba - Método de Newton
        self.newtonMethodTab = NewtonMethodTab()
        self.tabs.addTab(self.newtonMethodTab, "Método de Newton")

        # Segunda aba - Descida de Gradiente
        self.gradientDescentTab = GradientDescentTab()
        self.tabs.addTab(self.gradientDescentTab, "Descida de Gradiente")
