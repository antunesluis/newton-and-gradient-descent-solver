from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QFont


class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["n", "xn", "yn", "f(xn, yn)", "g(xn, yn)"])
        self.fill_table(self.newton_method_progression())

        # Ajustar o tamanho das células
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

        font = self.font()
        font.setPointSize(15)
        self.setFont(font)

        # Configurar os cabeçalhos para se expandirem conforme o espaço disponível
        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # type: ignore

    def newton_method_progression(self):
        # Exemplo de dados de progressão do método de Newton
        data = [
            [0, 1.0, 1.0, 0.5, 0.5],
            [1, 0.75, 0.75, 0.25, 0.25],
            [2, 0.5, 0.5, 0.1, 0.1],
            [3, 0.25, 0.25, 0.05, 0.05],
            [4, 0.1, 0.1, 0.01, 0.01],
        ]
        return data

    def fill_table(self, data):
        self.setRowCount(len(data))
        font = QFont()
        font.setPointSize(12)  # Ajuste o tamanho da fonte conforme necessário

        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setFont(font)
                self.setItem(row_idx, col_idx, item)
