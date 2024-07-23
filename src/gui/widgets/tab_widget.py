from PySide6.QtWidgets import QGridLayout, QWidget, QVBoxLayout, QTabWidget
from gui.widgets.newton_method_tab import NewtonMethodTab


class TabWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # Primeira aba - Método de Newton
        self.newton_method_tab = NewtonMethodTab()
        self.tabs.addTab(self.newton_method_tab, "Método de Newton")

        # Segunda aba - backpropagation
        self.tab2 = QWidget()
        self.tab2_layout = QGridLayout(self.tab2)
        self.tabs.addTab(self.tab2, "Backpropagation")
