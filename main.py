from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from tablewidget import Ui_MainWindow
import sys


class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.save_button.clicked.connect(self.data_save)
        self.ui.tableWidget.doubleClicked.connect (self.doubleClick)

    def doubleClick(self):
        for item in self.ui.tableWidget.selectedItems():
            print(item.row(), item.column(), item.text())

    def data_save(self):
        name = self.ui.line_name.text()
        price = self.ui.line_price.text()

        if name and price is not None:
            rowCount = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowCount)
            self.ui.tableWidget.setItem(rowCount,0,QTableWidgetItem(name))
            self.ui.tableWidget.setItem(rowCount,1,QTableWidgetItem(price))

    def loadProducts(self):

        products = [
            {'name':'Phone 1', 'price':1000},
            {'name': 'Phone 2', 'price': 2000},
            {'name': 'Phone 3', 'price': 3000},
            {'name': 'Phone 4', 'price': 4000},
        ]

        self.ui.tableWidget.setRowCount(len(products))
        self.ui.tableWidget.setColumnCount(2)

        self.ui.tableWidget.setHorizontalHeaderLabels(('Brand','Price'))

        self.ui.tableWidget.setColumnWidth(0,120)
        self.ui.tableWidget.setColumnWidth(1,50)


        row_index = 0
        for product in products:
            self.ui.tableWidget.setItem(row_index,0,QTableWidgetItem(str(product['name'])))
            self.ui.tableWidget.setItem(row_index,1,QTableWidgetItem(str(product['price'])))
            row_index += 1


def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

create_app()
