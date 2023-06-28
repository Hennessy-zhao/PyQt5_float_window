# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from index_ui import Ui_Form
from Dialog import Dialog
import sys


class IndexPane(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)  # 显示UI

    # 显示事件函数 设置初始显示内容
    def showEvent(self, QShowEvent):
        self.create_widget()

        self.dailog=Dialog(self)

    # 关闭界面触发函数
    def closeEvent(self, QCloseEvent):
        self.dailog.close()


    def create_widget(self):
        self.widget_1=QWidget(self)
        self.widget_1.setObjectName("widget_1")
        self.widget_1.setStyleSheet("#widget_1{background-color: rgba(255, 255, 255,0.3);border-radius : 10px;}")

        self.widget_1.raise_()          #控件在最顶层
        self.widget_1.setGeometry(100,150,int(self.width()*0.8),int(self.height()*0.3))     #设置横纵坐标、长宽

        self.hor_1=QHBoxLayout(self.widget_1)   #定义横向布局

        self.label_1=QLabel()
        self.label_1.setObjectName("label_1")
        self.label_1.setText("测试信息啦啦啦测试信息啦啦啦测试信啦啦啦测试信息啦啦啦测试信啦啦啦测试信息啦啦啦测试信啦啦啦测试信息啦啦啦测试信")
        self.label_1.setWordWrap(True)      #自动换行

        self.hor_1.addWidget(self.label_1)      #布局中添加控件


    def showWidget(self):
        self.widget_1.setVisible(True)

    def hideWidget(self):
        self.widget_1.setVisible(False)


    def showWindow(self):
        self.dailog.raise_()

        self.dailog.show()
        self.dailog.set_label("6666666")


    def hideWindow(self):
        self.dailog.close()


if __name__=='__main__':
    app = QApplication(sys.argv)

    form = IndexPane()
    form.show()

    sys.exit(app.exec_())
