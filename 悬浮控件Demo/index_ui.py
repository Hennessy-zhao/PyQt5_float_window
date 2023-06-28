# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(722, 440)
        Form.setStyleSheet("#Form{\n"
"    background-color: rgb(85, 170, 0);\n"
"}\n"
"\n"
"#widget_1{\n"
"    background-color: rgba(255, 255, 255,0.3);\n"
"    border-radius : 10px;\n"
"}\n"
"\n"
"#label_1{\n"
"    margin-left : 100px;\n"
"    font: 75 12pt \"微软雅黑\";\n"
"\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.showWidget)
        self.pushButton_2.clicked.connect(Form.showWindow)
        self.pushButton_4.clicked.connect(Form.hideWidget)
        self.pushButton_3.clicked.connect(Form.hideWindow)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "显示悬浮"))
        self.pushButton_4.setText(_translate("Form", "隐藏悬浮"))
        self.pushButton_2.setText(_translate("Form", "显示窗口"))
        self.pushButton_3.setText(_translate("Form", "隐藏窗口"))

