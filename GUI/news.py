# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\news.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#pour accéder au dossier parent
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from newsAPI import getNews

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1300, 776)
        self.NewsText = QtWidgets.QLabel(Dialog)
        self.NewsText.setGeometry(QtCore.QRect(280, 10, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.NewsText.setFont(font)
        self.NewsText.setObjectName("NewsText")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 1271, 731))
        self.groupBox.setObjectName("groupBox")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(0, 20, 1261, 711))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1259, 709))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 140, 1241, 141))
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(138, 138, 138))
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 420, 1241, 141))
        self.tableWidget_5.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(138, 138, 138))
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 280, 1241, 141))
        self.tableWidget_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(138, 138, 138))
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1241, 141))
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 141))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(138, 138, 138))
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 560, 1241, 151))
        self.tableWidget_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(138, 138, 138))
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(370, 0, 201, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.NewsText.setText(_translate("Dialog", "News"))
        self.groupBox.setTitle(_translate("Dialog", "News"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Title"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Information"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Source"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Date"))
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Title"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Information"))
        item = self.tableWidget_5.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Source"))
        item = self.tableWidget_5.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Date"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Title"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Information"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Source"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Date"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Title"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Information"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Source"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Date"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Title"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Information"))
        item = self.tableWidget_4.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Source"))
        item = self.tableWidget_4.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Date"))
        #intégration de la fonction qui va récupérer les news
        #récupération des variables
        articles = getNews()
        #création des items dans les cellules
        #article 1
        for i in range(0,4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
        #article 2
        for i in range(0,4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 0, item)
        #article 3
        for i in range(0,4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 0, item)
        #article 4
        for i in range(0,4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_4.setItem(i, 0, item)
        #article 5
        for i in range(0,4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_5.setItem(i, 0, item)
        #article 1
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)      
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        for i in range(0,4):
            self.tableWidget.setColumnWidth(i, 1150)
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("Dialog", articles[0][i]))
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setVisible(False)
        #article 2
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)      
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        for i in range(0,4):
            self.tableWidget_2.setColumnWidth(i, 1150)
            self.tableWidget_2.setItem(i, 0, item)
            item = self.tableWidget_2.item(i, 0)
            item.setText(_translate("Dialog", articles[1][i]))
        self.tableWidget_2.resizeRowsToContents()
        self.tableWidget_2.horizontalHeader().setVisible(False)
        #article 3
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)      
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        for i in range(0,4):
            self.tableWidget_3.setColumnWidth(i, 1150)
            self.tableWidget_3.setItem(i, 0, item)
            item = self.tableWidget_3.item(i, 0)
            item.setText(_translate("Dialog", articles[2][i]))
        self.tableWidget_3.resizeRowsToContents()
        self.tableWidget_3.horizontalHeader().setVisible(False)
        #article 4
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)      
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        for i in range(0,4):
            self.tableWidget_4.setColumnWidth(i, 1150)
            self.tableWidget_4.setItem(i, 0, item)
            item = self.tableWidget_4.item(i, 0)
            item.setText(_translate("Dialog", articles[3][i]))
        self.tableWidget_4.resizeRowsToContents()
        self.tableWidget_4.horizontalHeader().setVisible(False)
        #article 5
        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)      
        self.tableWidget_5.setSortingEnabled(__sortingEnabled)
        for i in range(0,4):
            self.tableWidget_5.setColumnWidth(i, 1150)
            self.tableWidget_5.setItem(i, 0, item)
            item = self.tableWidget_5.item(i, 0)
            item.setText(_translate("Dialog", articles[4][i]))
        self.tableWidget_5.resizeRowsToContents()
        self.tableWidget_5.horizontalHeader().setVisible(False)
        self.commandLinkButton.setText(_translate("Dialog", "https://messari.io/news"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

