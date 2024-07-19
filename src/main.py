import sys
from PySide6.QtWidgets import QApplication
from gui.widgets.main_window import MainWindow
from gui.widgets.styles import setupTheme

if __name__ == "__main__":
    app = QApplication(sys.argv)

    setupTheme(app)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
