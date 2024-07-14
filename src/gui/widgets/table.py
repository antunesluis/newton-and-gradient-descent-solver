from PySide6.QtWidgets import QTableWidget, QTableWidgetItem


class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["n", "xn", "yn", "f(xn, yn)", "g(xn, yn)"])
        self.fill_table(self.newton_method_progression())

        # Ajustar o tamanho das células
        self.setCellSizes(50, 100)  # Ajuste os valores conforme necessário

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
        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.setItem(row_idx, col_idx, item)

    def setCellSizes(self, row_height, column_width):
        for row in range(self.rowCount()):
            self.setRowHeight(row, row_height)
        for column in range(self.columnCount()):
            self.setColumnWidth(column, column_width)
