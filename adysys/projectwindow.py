# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adysys/src/pyqt/projectwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import Qsci
from PyQt5 import QtWebEngineWidgets
import sip

import time


class ProjectWindow(QtWidgets.QMainWindow):
    def __init__(self, qApp: QtWidgets.QApplication, project_path):
        super(ProjectWindow, self).__init__()
        self.app = qApp
        self.ProjectPath = project_path
        self.app.aboutToQuit.connect(self.destryer)

        self.ui = QtWidgets.QMainWindow()
        self._setupUI()
        self.ui.show()
        self.initProject()
        self.app.exec_()

    def initProject(self):
        qUrl = QtCore.QUrl(
            'http://127.0.0.1:6910/project?path={0}'.format(self.ProjectPath))
        # qUrl=QtCore.QUrl('http://193.30.96.18:3001')

        self.ProjectWebBrowser.setUrl(qUrl)
        self.ProjectWebBrowser.loadFinished.connect(self.ProjectLoaded)

    def ProjectLoaded(self):
        self.ProjectWebBrowser.page().toHtml(self.getPageContent)

    def getPageContent(self, data):
        self.html = data
        print(self.html)

    def _setupUI(self):

        self.ui.setObjectName('AdySysGUIMainWindow')

        self.ui.setWindowTitle('AdySys HTML UI')
        # - add Central Widget
        self.CentralWidget = QtWidgets.QWidget(self.ui)
        self.CentralWidget.setObjectName("AdySysGUICentralWidget")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.CentralWidget.sizePolicy().hasHeightForWidth())
        # Define Layout
        self.CentralWidgetLayout = QtWidgets.QGridLayout(self.CentralWidget)
        self.CentralWidgetLayout.setObjectName('CentralWidgetLayout')
        self.ui.setCentralWidget(self.CentralWidget)

        # Define MDI Work Area
        self.WorkAreaMDI = QtWidgets.QMdiArea(self.CentralWidget)
        self.WorkAreaMDI.setObjectName('AdySysGUIMDIWorkArea')
        self.CentralWidgetLayout.addWidget(self.WorkAreaMDI, 1, 0, 1, 1)
        self.WorkAreaMDI.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.WorkAreaMDI.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)

        # Define Browser MdiChild
        # - Keep this for later since we are going to be adding new stuff in here make it flexible to add Children dynamically
        # for now am going to set main browser that connects to path
        # /project?path=/project/path
        self.ProjectWebBrowserMDI = QtWidgets.QWidget()
        self.ProjectWebBrowserMDI.setObjectName('ProjectMainWebBrowser')
        self.ProjectWebBrowserMDI.setWindowTitle('Main App Browser')
        sizepolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding)
        sizepolicy.setVerticalStretch(0)
        sizepolicy.setHorizontalStretch(0)
        self.ProjectWebBrowserMDI.setSizePolicy(sizepolicy)

        # Define Browser WIndow (WebView)
        self.ProjectWebBrowser = QtWebEngineWidgets.QWebEngineView(
            self.ProjectWebBrowserMDI)
        self.ProjectWebBrowser.setMinimumWidth(
            self.ProjectWebBrowserMDI.width())
        self.ProjectWebBrowser.setMinimumHeight(
            self.ProjectWebBrowserMDI.height())

        # Define Browser MdiChild Layout
        # Add ProjectBrowser to the Layout
        self.ProjectWebBrowserLayout = QtWidgets.QGridLayout(
            self.ProjectWebBrowserMDI)

        self.ProjectWebBrowserLayout.addWidget(
            self.ProjectWebBrowser, 0, 0, 1, 1)

        self.WorkAreaMDI.addSubWindow(self.ProjectWebBrowserMDI)
        self.ProjectWebBrowserMDI.show()

        # Define ToolBox
        self.ProjectToolBox = QtWidgets.QDockWidget(self.ui)
        self.ProjectToolBox.setObjectName('AdySysToolBox')
        self.ProjectToolBox.setWindowTitle('ToolBox')
        self.ProjectToolBox.setFloating(False)
        # Define size policy
        sizepolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding)
        sizepolicy.setHorizontalStretch(0)
        sizepolicy.setVerticalStretch(0)
        sizepolicy.setHeightForWidth(True)
        self.ProjectToolBox.setSizePolicy(sizepolicy)
        self.ui.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.ProjectToolBox)
        # Define ToolBox Widgets

    def resizeEvent(self, QResizeEvent):
        print(QResizeEvent)

    def destryer(self):
        if not sip.isdeleted(self.ProjectWebBrowserMDI):
            self.ProjectWebBrowserMDI.deleteLater()
        # print('Destroying Window')


def start_gui(project):
    app = QtWidgets.QApplication(sys.argv)
    ProjectWindow(app, project)


if __name__ == '__main__':
    # '''
    # - define an object of type qtcore
    # '''
    # app = QtWidgets.QApplication(sys.argv)
    # projectwindow = QtWidgets.QMainWindow()
    # ui = ProjectWindow(projectwindow)
    # app.aboutToQuit.connect(ui.destryer)
    # # ui.setupUi(projectwindow)
    # # projectwindow.show()
    # sys.exit(app.exec_())
    start_gui('/tmp/project/testproject')
