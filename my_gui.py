# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_gui.ui'
#
# Created: Sat Jul  4 17:43:08 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(636, 497)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/app-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.toolButton_zoom_out = QtGui.QToolButton(self.centralwidget)
        self.toolButton_zoom_out.setEnabled(True)
        self.toolButton_zoom_out.setStyleSheet(_fromUtf8("QToolButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color:rgb(193, 210, 238)\n"
"}"))
        self.toolButton_zoom_out.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/zoom-out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_zoom_out.setIcon(icon1)
        self.toolButton_zoom_out.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_zoom_out.setObjectName(_fromUtf8("toolButton_zoom_out"))
        self.horizontalLayout_2.addWidget(self.toolButton_zoom_out)
        self.horizontalSlider_zoom = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_zoom.setAutoFillBackground(False)
        self.horizontalSlider_zoom.setMinimum(100)
        self.horizontalSlider_zoom.setMaximum(1100)
        self.horizontalSlider_zoom.setProperty("value", 600)
        self.horizontalSlider_zoom.setSliderPosition(600)
        self.horizontalSlider_zoom.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_zoom.setInvertedAppearance(False)
        self.horizontalSlider_zoom.setInvertedControls(False)
        self.horizontalSlider_zoom.setObjectName(_fromUtf8("horizontalSlider_zoom"))
        self.horizontalLayout_2.addWidget(self.horizontalSlider_zoom)
        self.toolButton_zoom_in = QtGui.QToolButton(self.centralwidget)
        self.toolButton_zoom_in.setEnabled(True)
        self.toolButton_zoom_in.setStyleSheet(_fromUtf8("QToolButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color:rgb(193, 210, 238)\n"
"}"))
        self.toolButton_zoom_in.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/zoom-in.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_zoom_in.setIcon(icon2)
        self.toolButton_zoom_in.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_zoom_in.setObjectName(_fromUtf8("toolButton_zoom_in"))
        self.horizontalLayout_2.addWidget(self.toolButton_zoom_in)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.toolButton_previous = QtGui.QToolButton(self.centralwidget)
        self.toolButton_previous.setStyleSheet(_fromUtf8("QToolButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color:rgb(193, 210, 238)\n"
"}"))
        self.toolButton_previous.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_previous.setIcon(icon3)
        self.toolButton_previous.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_previous.setCheckable(False)
        self.toolButton_previous.setChecked(False)
        self.toolButton_previous.setAutoExclusive(True)
        self.toolButton_previous.setObjectName(_fromUtf8("toolButton_previous"))
        self.horizontalLayout.addWidget(self.toolButton_previous)
        self.toolButton_next = QtGui.QToolButton(self.centralwidget)
        self.toolButton_next.setStyleSheet(_fromUtf8("QToolButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color:rgb(193, 210, 238)\n"
"}"))
        self.toolButton_next.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_next.setIcon(icon4)
        self.toolButton_next.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_next.setCheckable(False)
        self.toolButton_next.setChecked(False)
        self.toolButton_next.setAutoExclusive(True)
        self.toolButton_next.setObjectName(_fromUtf8("toolButton_next"))
        self.horizontalLayout.addWidget(self.toolButton_next)
        self.toolButton_fit_in_view = QtGui.QToolButton(self.centralwidget)
        self.toolButton_fit_in_view.setStyleSheet(_fromUtf8("QToolButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color:rgb(193, 210, 238)\n"
"}"))
        self.toolButton_fit_in_view.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/fullscreen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_fit_in_view.setIcon(icon5)
        self.toolButton_fit_in_view.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_fit_in_view.setCheckable(False)
        self.toolButton_fit_in_view.setChecked(False)
        self.toolButton_fit_in_view.setObjectName(_fromUtf8("toolButton_fit_in_view"))
        self.horizontalLayout.addWidget(self.toolButton_fit_in_view)
        self.toolButton_rotateCW = QtGui.QToolButton(self.centralwidget)
        self.toolButton_rotateCW.setStyleSheet(_fromUtf8("QToolButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color:rgb(193, 210, 238)\n"
"}"))
        self.toolButton_rotateCW.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/rotate-CW.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_rotateCW.setIcon(icon6)
        self.toolButton_rotateCW.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_rotateCW.setCheckable(False)
        self.toolButton_rotateCW.setChecked(False)
        self.toolButton_rotateCW.setAutoExclusive(True)
        self.toolButton_rotateCW.setObjectName(_fromUtf8("toolButton_rotateCW"))
        self.horizontalLayout.addWidget(self.toolButton_rotateCW)
        self.toolButton_rotateCCW = QtGui.QToolButton(self.centralwidget)
        self.toolButton_rotateCCW.setStyleSheet(_fromUtf8("QToolButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color:rgb(193, 210, 238)\n"
"}"))
        self.toolButton_rotateCCW.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/rotate-CCW.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_rotateCCW.setIcon(icon7)
        self.toolButton_rotateCCW.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_rotateCCW.setCheckable(False)
        self.toolButton_rotateCCW.setChecked(False)
        self.toolButton_rotateCCW.setAutoExclusive(True)
        self.toolButton_rotateCCW.setObjectName(_fromUtf8("toolButton_rotateCCW"))
        self.horizontalLayout.addWidget(self.toolButton_rotateCCW)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFiel = QtGui.QMenu(self.menubar)
        self.menuFiel.setObjectName(_fromUtf8("menuFiel"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(self.dockWidgetContents)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionFile_explorer = QtGui.QAction(MainWindow)
        self.actionFile_explorer.setObjectName(_fromUtf8("actionFile_explorer"))
        self.menuFiel.addAction(self.actionLoad)
        self.menuFiel.addAction(self.actionExit)
        self.menuView.addAction(self.actionFile_explorer)
        self.menubar.addAction(self.menuFiel.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PyImView", None))
        self.toolButton_zoom_out.setToolTip(_translate("MainWindow", "Zoom out", None))
        self.horizontalSlider_zoom.setToolTip(_translate("MainWindow", "Zoom in/out slider", None))
        self.toolButton_zoom_in.setToolTip(_translate("MainWindow", "Zoom in ", None))
        self.toolButton_previous.setToolTip(_translate("MainWindow", "Previous picture", None))
        self.toolButton_next.setToolTip(_translate("MainWindow", "Next picture", None))
        self.toolButton_fit_in_view.setToolTip(_translate("MainWindow", "Fit in view", None))
        self.toolButton_rotateCW.setToolTip(_translate("MainWindow", "Rotate clockwise (CW)", None))
        self.toolButton_rotateCCW.setToolTip(_translate("MainWindow", "Rotate counter-clockwise (CCW)", None))
        self.menuFiel.setTitle(_translate("MainWindow", "File", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "File explorer", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionFile_explorer.setText(_translate("MainWindow", "File explorer", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

