# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_projectwindow(object):
    def setupUi(self, projectwindow):
        projectwindow.setObjectName("projectwindow")
        projectwindow.resize(971, 711)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/browser/browser.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        projectwindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(projectwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.projectwindowbrowser = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.projectwindowbrowser.setUrl(QtCore.QUrl("http://html5test.com/"))
        self.projectwindowbrowser.setObjectName("projectwindowbrowser")
        self.gridLayout.addWidget(self.projectwindowbrowser, 0, 0, 1, 1)
        projectwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(projectwindow)
        QtCore.QMetaObject.connectSlotsByName(projectwindow)

    def retranslateUi(self, projectwindow):
        _translate = QtCore.QCoreApplication.translate
        projectwindow.setWindowTitle(_translate("projectwindow", "Project Window"))
from PyQt5 import QtWebEngineWidgets
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    projectwindow = QtWidgets.QMainWindow()
    ui = Ui_projectwindow()
    ui.setupUi(projectwindow)
    projectwindow.show()
    sys.exit(app.exec_())
