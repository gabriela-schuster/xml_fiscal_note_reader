import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Leitor de Notas")
        self.setGeometry(100, 100, 400, 200)

        button = QPushButton("Abrir Arquivo XML", self)
        button.setGeometry(200, 80, 100, 30)
        button.clicked.connect(self.open_file_dialog)


    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "XML Files (*.xml)", options=options)
        if file_name:
            print(file_name)

        # TODO: pass file path to function that reads it


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
