# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ioan/PycharmProjects/hackathon/src/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 482)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.masterFrame = QtWidgets.QFrame(self.centralwidget)
        self.masterFrame.setGeometry(QtCore.QRect(-10, 0, 1011, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.masterFrame.sizePolicy().hasHeightForWidth())
        self.masterFrame.setSizePolicy(sizePolicy)
        self.masterFrame.setObjectName("masterFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.masterFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.masterLayout = QtWidgets.QVBoxLayout()
        self.masterLayout.setObjectName("masterLayout")
        self.topFrame = QtWidgets.QFrame(self.masterFrame)
        self.topFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.topFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 981, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.topDivision = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.topDivision.setContentsMargins(10, 10, 10, 10)
        self.topDivision.setSpacing(10)
        self.topDivision.setObjectName("topDivision")
        self.todayFrame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.todayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.todayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.todayFrame.setObjectName("todayFrame")
        self.todayWidget = QtWidgets.QWidget(self.todayFrame)
        self.todayWidget.setGeometry(QtCore.QRect(-1, -1, 311, 201))
        self.todayWidget.setObjectName("todayWidget")
        self.todayLabel = QtWidgets.QLabel(self.todayWidget)
        self.todayLabel.setGeometry(QtCore.QRect(120, 10, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.todayLabel.setFont(font)
        self.todayLabel.setObjectName("todayLabel")
        self.todayTable = QtWidgets.QTableWidget(self.todayWidget)
        self.todayTable.setGeometry(QtCore.QRect(10, 70, 291, 120))
        self.todayTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.todayTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.todayTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.todayTable.setTextElideMode(QtCore.Qt.ElideRight)
        self.todayTable.setShowGrid(True)
        self.todayTable.setGridStyle(QtCore.Qt.SolidLine)
        self.todayTable.setColumnCount(2)
        self.todayTable.setObjectName("todayTable")
        self.todayTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.todayTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.todayTable.setHorizontalHeaderItem(1, item)
        self.todayRecipe = QtWidgets.QLabel(self.todayWidget)
        self.todayRecipe.setGeometry(QtCore.QRect(20, 40, 121, 21))
        self.todayRecipe.setObjectName("todayRecipe")
        self.topDivision.addWidget(self.todayFrame)
        self.tommorowFrame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.tommorowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tommorowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tommorowFrame.setObjectName("tommorowFrame")
        self.tommorowWidget = QtWidgets.QWidget(self.tommorowFrame)
        self.tommorowWidget.setGeometry(QtCore.QRect(0, 0, 311, 201))
        self.tommorowWidget.setObjectName("tommorowWidget")
        self.tommorowLabel = QtWidgets.QLabel(self.tommorowWidget)
        self.tommorowLabel.setGeometry(QtCore.QRect(120, 10, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.tommorowLabel.setFont(font)
        self.tommorowLabel.setObjectName("tommorowLabel")
        self.tommorrowTable = QtWidgets.QTableWidget(self.tommorowWidget)
        self.tommorrowTable.setGeometry(QtCore.QRect(10, 70, 291, 120))
        self.tommorrowTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tommorrowTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tommorrowTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tommorrowTable.setTextElideMode(QtCore.Qt.ElideRight)
        self.tommorrowTable.setShowGrid(True)
        self.tommorrowTable.setGridStyle(QtCore.Qt.SolidLine)
        self.tommorrowTable.setColumnCount(2)
        self.tommorrowTable.setObjectName("tommorrowTable")
        self.tommorrowTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tommorrowTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tommorrowTable.setHorizontalHeaderItem(1, item)
        self.tommorowRecipe = QtWidgets.QLabel(self.tommorowWidget)
        self.tommorowRecipe.setGeometry(QtCore.QRect(10, 40, 171, 21))
        self.tommorowRecipe.setObjectName("tommorowRecipe")
        self.topDivision.addWidget(self.tommorowFrame)
        self.dayAfterFrame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.dayAfterFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dayAfterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dayAfterFrame.setObjectName("dayAfterFrame")
        self.dayAfterWidget = QtWidgets.QWidget(self.dayAfterFrame)
        self.dayAfterWidget.setGeometry(QtCore.QRect(-1, -1, 311, 201))
        self.dayAfterWidget.setObjectName("dayAfterWidget")
        self.dayAfterLabel = QtWidgets.QLabel(self.dayAfterWidget)
        self.dayAfterLabel.setGeometry(QtCore.QRect(80, 10, 181, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.dayAfterLabel.setFont(font)
        self.dayAfterLabel.setObjectName("dayAfterLabel")
        self.dayAfterTable = QtWidgets.QTableWidget(self.dayAfterWidget)
        self.dayAfterTable.setGeometry(QtCore.QRect(10, 70, 291, 120))
        self.dayAfterTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.dayAfterTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dayAfterTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dayAfterTable.setTextElideMode(QtCore.Qt.ElideRight)
        self.dayAfterTable.setShowGrid(True)
        self.dayAfterTable.setGridStyle(QtCore.Qt.SolidLine)
        self.dayAfterTable.setColumnCount(2)
        self.dayAfterTable.setObjectName("dayAfterTable")
        self.dayAfterTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dayAfterTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dayAfterTable.setHorizontalHeaderItem(1, item)
        self.dayAfterRecipe = QtWidgets.QLabel(self.dayAfterWidget)
        self.dayAfterRecipe.setGeometry(QtCore.QRect(10, 40, 251, 21))
        self.dayAfterRecipe.setObjectName("dayAfterRecipe")
        self.topDivision.addWidget(self.dayAfterFrame)
        self.masterLayout.addWidget(self.topFrame)
        self.bottomFrame = QtWidgets.QFrame(self.masterFrame)
        self.bottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomFrame.setObjectName("bottomFrame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.bottomFrame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 981, 231))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.bottomDivision = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.bottomDivision.setContentsMargins(10, 10, 10, 10)
        self.bottomDivision.setSpacing(10)
        self.bottomDivision.setObjectName("bottomDivision")
        self.foodlListFrame = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.foodlListFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.foodlListFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.foodlListFrame.setObjectName("foodlListFrame")
        self.ItemsTable = QtWidgets.QTableWidget(self.foodlListFrame)
        self.ItemsTable.setGeometry(QtCore.QRect(140, 10, 381, 191))
        self.ItemsTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ItemsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ItemsTable.setGridStyle(QtCore.Qt.SolidLine)
        self.ItemsTable.setRowCount(0)
        self.ItemsTable.setColumnCount(2)
        self.ItemsTable.setObjectName("ItemsTable")
        item = QtWidgets.QTableWidgetItem()
        self.ItemsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ItemsTable.setHorizontalHeaderItem(1, item)
        self.ItemsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.listEditFrame = QtWidgets.QFrame(self.foodlListFrame)
        self.listEditFrame.setEnabled(True)
        self.listEditFrame.setGeometry(QtCore.QRect(664, 0, 291, 211))
        self.listEditFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listEditFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listEditFrame.setObjectName("listEditFrame")
        self.editMenu = QtWidgets.QWidget(self.listEditFrame)
        self.editMenu.setGeometry(QtCore.QRect(10, 10, 271, 191))
        self.editMenu.setObjectName("editMenu")
        self.editorTab = QtWidgets.QTabWidget(self.editMenu)
        self.editorTab.setGeometry(QtCore.QRect(0, 0, 401, 191))
        self.editorTab.setFocusPolicy(QtCore.Qt.TabFocus)
        self.editorTab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.editorTab.setTabPosition(QtWidgets.QTabWidget.North)
        self.editorTab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.editorTab.setElideMode(QtCore.Qt.ElideNone)
        self.editorTab.setObjectName("editorTab")
        self.Add = QtWidgets.QWidget()
        self.Add.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.Add.setObjectName("Add")
        self.itemAddLabel = QtWidgets.QLabel(self.Add)
        self.itemAddLabel.setGeometry(QtCore.QRect(10, 20, 80, 21))
        self.itemAddLabel.setObjectName("itemAddLabel")
        self.addItemBox = QtWidgets.QLineEdit(self.Add)
        self.addItemBox.setGeometry(QtCore.QRect(100, 10, 161, 29))
        self.addItemBox.setObjectName("addItemBox")
        self.quantityAddLabel_2 = QtWidgets.QLabel(self.Add)
        self.quantityAddLabel_2.setGeometry(QtCore.QRect(10, 60, 80, 21))
        self.quantityAddLabel_2.setObjectName("quantityAddLabel_2")
        self.addGramsBox = QtWidgets.QLineEdit(self.Add)
        self.addGramsBox.setGeometry(QtCore.QRect(102, 50, 161, 29))
        self.addGramsBox.setObjectName("addGramsBox")
        self.addItemButton = QtWidgets.QPushButton(self.Add)
        self.addItemButton.setGeometry(QtCore.QRect(80, 100, 106, 30))
        self.addItemButton.setDefault(False)
        self.addItemButton.setFlat(False)
        self.addItemButton.setObjectName("addItemButton")
        self.editorTab.addTab(self.Add, "")
        self.Edit = QtWidgets.QWidget()
        self.Edit.setObjectName("Edit")
        self.itemEditLabel = QtWidgets.QLabel(self.Edit)
        self.itemEditLabel.setGeometry(QtCore.QRect(10, 20, 80, 21))
        self.itemEditLabel.setObjectName("itemEditLabel")
        self.quantityEditLabel = QtWidgets.QLabel(self.Edit)
        self.quantityEditLabel.setGeometry(QtCore.QRect(10, 60, 80, 21))
        self.quantityEditLabel.setObjectName("quantityEditLabel")
        self.editFromPantry = QtWidgets.QListWidget(self.Edit)
        self.editFromPantry.setGeometry(QtCore.QRect(100, 10, 161, 31))
        self.editFromPantry.setTabKeyNavigation(True)
        self.editFromPantry.setProperty("showDropIndicator", True)
        self.editFromPantry.setAlternatingRowColors(True)
        self.editFromPantry.setProperty("isWrapping", False)
        self.editFromPantry.setUniformItemSizes(True)
        self.editFromPantry.setObjectName("editFromPantry")
        self.editGramsBox = QtWidgets.QLineEdit(self.Edit)
        self.editGramsBox.setGeometry(QtCore.QRect(100, 50, 161, 29))
        self.editGramsBox.setObjectName("editGramsBox")
        self.confirmChangeButton = QtWidgets.QPushButton(self.Edit)
        self.confirmChangeButton.setGeometry(QtCore.QRect(70, 100, 141, 30))
        self.confirmChangeButton.setDefault(False)
        self.confirmChangeButton.setFlat(False)
        self.confirmChangeButton.setObjectName("confirmChangeButton")
        self.editorTab.addTab(self.Edit, "")
        self.Remove = QtWidgets.QWidget()
        self.Remove.setObjectName("Remove")
        self.itemRemoveLabel = QtWidgets.QLabel(self.Remove)
        self.itemRemoveLabel.setGeometry(QtCore.QRect(10, 20, 80, 21))
        self.itemRemoveLabel.setObjectName("itemRemoveLabel")
        self.deleteFromPantry = QtWidgets.QListWidget(self.Remove)
        self.deleteFromPantry.setGeometry(QtCore.QRect(100, 10, 151, 31))
        self.deleteFromPantry.setTabKeyNavigation(True)
        self.deleteFromPantry.setProperty("showDropIndicator", True)
        self.deleteFromPantry.setAlternatingRowColors(True)
        self.deleteFromPantry.setProperty("isWrapping", False)
        self.deleteFromPantry.setUniformItemSizes(True)
        self.deleteFromPantry.setObjectName("deleteFromPantry")
        self.removeItemButton = QtWidgets.QPushButton(self.Remove)
        self.removeItemButton.setGeometry(QtCore.QRect(70, 90, 141, 30))
        self.removeItemButton.setDefault(False)
        self.removeItemButton.setFlat(False)
        self.removeItemButton.setObjectName("removeItemButton")
        self.editorTab.addTab(self.Remove, "")
        self.bottomDivision.addWidget(self.foodlListFrame)
        self.masterLayout.addWidget(self.bottomFrame)
        self.verticalLayout_4.addLayout(self.masterLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.editorTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ItemsTable, self.editorTab)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SCRAN"))
        self.todayLabel.setText(_translate("MainWindow", "Today"))
        item = self.todayTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ITEM"))
        item = self.todayTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "AMOUNT"))
        self.todayRecipe.setText(_translate("MainWindow", "Today\'s Recipe"))
        self.tommorowLabel.setText(_translate("MainWindow", "Tommrow"))
        item = self.tommorrowTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ITEM"))
        item = self.tommorrowTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "AMOUNT"))
        self.tommorowRecipe.setText(_translate("MainWindow", "Tommorow\'s Recipe"))
        self.dayAfterLabel.setText(_translate("MainWindow", "Day After Tommorow"))
        item = self.dayAfterTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ITEM"))
        item = self.dayAfterTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "AMOUNT"))
        self.dayAfterRecipe.setText(_translate("MainWindow", "Day After Tommorows Recipe"))
        self.ItemsTable.setSortingEnabled(True)
        item = self.ItemsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ITEM"))
        item = self.ItemsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "AMOUNT"))
        self.itemAddLabel.setText(_translate("MainWindow", "Item"))
        self.addItemBox.setPlaceholderText(_translate("MainWindow", "Enter an Item"))
        self.quantityAddLabel_2.setText(_translate("MainWindow", "Quantity"))
        self.addGramsBox.setPlaceholderText(_translate("MainWindow", "Enter grams"))
        self.addItemButton.setText(_translate("MainWindow", "Add Item"))
        self.editorTab.setTabText(self.editorTab.indexOf(self.Add), _translate("MainWindow", "Add"))
        self.itemEditLabel.setText(_translate("MainWindow", "Item"))
        self.quantityEditLabel.setText(_translate("MainWindow", "Quantity"))
        self.editFromPantry.setSortingEnabled(True)
        self.editGramsBox.setPlaceholderText(_translate("MainWindow", "Enter grams"))
        self.confirmChangeButton.setText(_translate("MainWindow", "Confirm Change"))
        self.editorTab.setTabText(self.editorTab.indexOf(self.Edit), _translate("MainWindow", "Edit"))
        self.itemRemoveLabel.setText(_translate("MainWindow", "Item"))
        self.deleteFromPantry.setSortingEnabled(True)
        self.removeItemButton.setText(_translate("MainWindow", "Remove Item"))
        self.editorTab.setTabText(self.editorTab.indexOf(self.Remove), _translate("MainWindow", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
