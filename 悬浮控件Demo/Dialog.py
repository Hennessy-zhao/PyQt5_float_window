# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtSql

from dialog_ui import Ui_Dialog

import sys


class Dialog(QDialog,Ui_Dialog):
    '''
        创建自定义信号
    '''
    connect_sql_signal = pyqtSignal()  # 需要检查数据库连接信号

    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowOpacity(0.3)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setupUi(self)      #显示UI

    # 显示事件函数 设置初始显示内容
    def showEvent(self, QShowEvent):

        self.setGeometry(self.parent().x() + 100, self.parent().y() + 150, int(self.parent().width() * 0.8),int(self.parent().height() * 0.3))

    def set_label(self,info):
        self.label_3.setText(info)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Dialog()
    form.show()
    sys.exit(app.exec_())