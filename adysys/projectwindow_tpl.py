# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adysys/src/pyqt/projectwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_projectwindow(object):
    def setupUi(self, projectwindow):
        projectwindow.setObjectName("projectwindow")
        projectwindow.resize(1172, 835)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/browser/browser.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        projectwindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(projectwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.project_work_area = QtWidgets.QMdiArea(self.centralwidget)
        self.project_work_area.setObjectName("project_work_area")
        self.project_browser = QtWidgets.QWidget()
        self.project_browser.setObjectName("project_browser")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.project_browser)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.WebView = QtWebEngineWidgets.QWebEngineView(self.project_browser)
        self.WebView.setUrl(QtCore.QUrl("about:blank"))
        self.WebView.setObjectName("WebView")
        self.gridLayout_2.addWidget(self.WebView, 0, 0, 1, 1)
        self.project_text_editor = QtWidgets.QWidget()
        self.project_text_editor.setObjectName("project_text_editor")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.project_text_editor)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textEdit = Qsci.QsciScintilla(self.project_text_editor)
        self.textEdit.setToolTip("")
        self.textEdit.setWhatsThis("")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_4.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.project_work_area, 1, 0, 1, 1)
        projectwindow.setCentralWidget(self.centralwidget)
        self.ToolBox = QtWidgets.QDockWidget(projectwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolBox.sizePolicy().hasHeightForWidth())
        self.ToolBox.setSizePolicy(sizePolicy)
        self.ToolBox.setMouseTracking(True)
        self.ToolBox.setFloating(False)
        self.ToolBox.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.ToolBox.setObjectName("ToolBox")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.treeWidget = QtWidgets.QTreeWidget(self.dockWidgetContents_2)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        brush = QtGui.QBrush(QtGui.QColor(166, 166, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item_0.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 38, 202))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout_3.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.ToolBox.setWidget(self.dockWidgetContents_2)
        projectwindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.ToolBox)

        self.retranslateUi(projectwindow)
        QtCore.QMetaObject.connectSlotsByName(projectwindow)

    def retranslateUi(self, projectwindow):
        _translate = QtCore.QCoreApplication.translate
        projectwindow.setWindowTitle(_translate("projectwindow", "Project Window"))
        self.project_browser.setWindowTitle(_translate("projectwindow", "LiveView"))
        self.project_text_editor.setWindowTitle(_translate("projectwindow", "Code"))
        self.ToolBox.setWindowTitle(_translate("projectwindow", "ToolBox"))
        self.treeWidget.headerItem().setText(0, _translate("projectwindow", "Widgets"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("projectwindow", "Button"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("projectwindow", "Button"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("projectwindow", "Link"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("projectwindow", "Push Button"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("projectwindow", "Input"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("projectwindow", "Text"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("projectwindow", "Text Area"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
from PyQt5 import Qsci
from PyQt5 import QtWebEngineWidgets
if __name__ == '__main__':
    import resources_rc
else:
    import adysys.resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    projectwindow = QtWidgets.QMainWindow()
    ui = Ui_projectwindow()
    ui.setupUi(projectwindow)
    projectwindow.show()
    sys.exit(app.exec_())
