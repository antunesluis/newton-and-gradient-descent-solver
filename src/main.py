import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicação PyQt6 Básica")

        # Criação de um widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()

        # Adicionando um rótulo
        label = QLabel("Olá, PyQt6!")
        layout.addWidget(label)

        # Aplicando o layout ao widget central
        central_widget.setLayout(layout)


# Inicialização da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
