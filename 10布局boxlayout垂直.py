# !/usr/bin/env zxx-python
# -- coding: utf-8 --
# author:albert time:2022-11-13
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        #调用父类的__init__的方法，因为它里面有很多对UI空间的初始化操作
        super().__init__()

        #设置大小
        self.resize(300,300)
        #设置标题
        self.setWindowTitle("垂直布局")

        #垂直布局
        layout=QVBoxLayout()

        #作用是在布局器中增加一个伸缩两，伸缩量，里面的参数表示QSpaceerItem的个数，默认值为零
        #会将你放在layout中的压缩成默认的大小
        #下面的比例是1：1：1：2
        layout.addStretch(1)

        btn1=QPushButton("按钮1")
        #添加到布局器中
        #layout.addWidget(btn1,Qt.AlignmentFlag.AlignTop)
        layout.addWidget(btn1)

        layout.addStretch(1)
        btn2 = QPushButton("按钮2")
        # 添加到布局器中
        layout.addWidget(btn2)

        layout.addStretch(1)
        btn3 = QPushButton("按钮3")
        # 添加到布局器中
        layout.addWidget(btn3)

        layout.addStretch(2)

        #让窗口按这个布局排列
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    # 设置窗口标题
    w.setWindowTitle("第unkown个PYQT")

    # 展示窗口
    w.show()

    # 程序进入循环等待状态
    app.exec_()