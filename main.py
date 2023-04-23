import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout
import xml.etree.ElementTree as ET

from get_data import get_data, clean_data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Leitor de Notas")
        self.setGeometry(100, 100, 400, 200)

        # Create a QWidget to hold both the button and the table widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)

        self.table = QTableWidget()

        button = QPushButton("Abrir Arquivo XML", self)
        button.setGeometry(200, 80, 100, 30)
        button.clicked.connect(self.open_file_dialog)

        layout.addWidget(button)
        layout.addWidget(self.table)


    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "XML Files (*.xml)", options=options)
        if file_name:
            data = get_data(file_name)
            self.show_data_table(data)


    def show_data_table(self, data):
        namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
        names = []

        for prod in data:
            name_element = prod.find('nfe:prod/nfe:xProd', namespaces)
            # print(name_element)
            names.append(clean_data(name_element))

        # set the number of rows and columns in the table
        self.table.setRowCount(len(names))
        self.table.setColumnCount(2)

        # set the headers for the rows and columns
        self.table.setHorizontalHeaderLabels(['Name', 'Age'])
        self.table.setVerticalHeaderLabels(names)

        # populate the table with data
        self.table.setItem(0, 0, QTableWidgetItem('John'))
        self.table.setItem(0, 1, QTableWidgetItem('30'))
        self.table.setItem(1, 0, QTableWidgetItem('Jane'))
        self.table.setItem(1, 1, QTableWidgetItem('25'))
        self.table.setItem(2, 0, QTableWidgetItem('Bob'))
        self.table.setItem(2, 1, QTableWidgetItem('40'))

        self.table.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
