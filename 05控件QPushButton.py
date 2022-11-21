#!/usr/bin/env zxx-python
# -- coding: utf-8 --
# author:albert time:2022-11-18
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget

if __name__ == '__main__':
    app=QApplication(sys.argv)

    w=QWidget()

    #设置窗口标题
    w.setWindowTitle("第一个PYQT")

    # #在窗口中创建控件
    # btn=QPushButton("按钮")
    #
    # #设置按钮的父亲是当前窗口，等于是添加到窗口显示
    # btn.setParent(w)

    # label=QLabel("账号：")#6----------------------------------------------------------
    # label.setParent(w)
    #纯文本
    label=QLabel("账号：",w)
    label.setGeometry(20,20,30,20)

    #文本框#7---------------------------------------------------------
    edit=QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(55,20,200,20)

    #在窗口里面添加控件
    btn=QPushButton("注册",w)
    btn.setGeometry(50,80,70,30)

    #----------------------8调整窗口大小位置--------------------------------
    # w.resize(300,300)
    # w.move(0,0)
    # #调整窗口在屏幕中央显示
    # center_pointer=QDesktopWidget().availableGeometry().center()
    # print(center_pointer)
    # x=center_pointer.x()
    # y=center_pointer.y()
    # # print(w.frameGeometry())
    # # print(w.frameGeometry().getRect())
    # # print(type(w.frameGeometry().getRect()))
    # old_x,old_y,width,height=w.frameGeometry().getRect()
    # w.move(int(x-width/2),int(y-height/2))#i add int

    #09设置窗口图标
    w.setWindowIcon(QIcon('sw.png'))
    from PyQt5 import Qt
    # self.setWindowFlags(Qt.Qt.CustomizeWindowHint)  # 去掉标题栏的代码
    # Qt.FramelessWindowHintc # todo 无法隐藏
    # setWindowFlags(self, type)


    #展示窗口
    w.show()

    #程序进入循环等待状态
    app.exec_()