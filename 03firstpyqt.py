# !/usr/bin/env zxx-python
# -- coding: utf-8 --
# author:albert time:2022-11-13
# url: https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/index.html#/README
import sys

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app=QApplication(sys.argv)

    w=QWidget()

    #设置窗口标题
    w.setWindowTitle("第一个PYQT")

    #展示窗口
    w.show()

    #程序进入循环等待状态
    app.exec_()