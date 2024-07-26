from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QFont


class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["n", "xn", "yn", "f(xn, yn)", "g(xn, yn)"])
        self.resizeColumnsToContents()

        self.resizeRowsToContents()

        header = self.horizontalHeader()
        headerFont = header.font()
        headerFont.setPixelSize(25)
        header.setFont(headerFont)
        header.setSectionResizeMode(QHeaderView.Stretch)  # type: ignore

    def update_table(self, data):
        self.setRowCount(len(data))
        font = QFont()
        font.setPointSize(12)

        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                if isinstance(col_data, (int, float)):
                    col_data = f"{col_data:.4f}"

                item = QTableWidgetItem(str(col_data))
                item.setFont(font)
                self.setItem(row_idx, col_idx, item)
