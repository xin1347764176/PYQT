import sys
import json
import time

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QThread,pyqtSignal
class LoginThread(QThread):
    #创建自定义信号
    start_login_signal=pyqtSignal(str)

    def __init__(self):
        super(LoginThread, self).__init__()

    def login_by_requests(self,user_password_json):
        # 将json字符串，转换为自定，从而实现传递了用户名及密码
        user_password_json = json.loads(user_password_json)
        print(user_password_json.get( "user_name" ))
        print(user_password_json.get("password"))

    def run(self):
        while True:
            print("子线程正在执行。。。")
            time.sleep(1)


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./QtDesiner/login-2.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件
        # print(self.ui)#谁？ui文件中最顶层的对象form
        # print(self.ui.label)
        # print(self.ui.label.text())

        # 提取要操作的控件
        self.user_name_qwidget = self.ui.lineEdit  # 用户名输入框
        self.password_qwidget = self.ui.lineEdit_2  # 密码输入框
        self.login_btn = self.ui.pushButton  # 登录按钮
        self.forget_password_btn = self.ui.pushButton_2  # 忘记密码按钮
        self.textBrowser = self.ui.textBrowser  # 文本显示区域

        # 绑定信号与槽函数
        self.login_btn.clicked.connect(self.login)

        # 创建一个子线程注意这里要将login_thread变量变为对象的属性，如果不是对象属性，而是一个普通的局部变量的话
        # 会随着init_ui函数执行结束而被释放况时夺线程还没有执行完毕所有会产生问题)
        self.login_thread=LoginThread()
        # 将要创建的子线程类中的信号进行绑定
        self.login_thread.start_login_signal.connect(self.login_thread.login_by_requests)
        #让子线程开始工作
        self.login_thread.start()

    def login(self):
        """登录按钮的槽函数"""
        user_name = self.user_name_qwidget.text()
        password = self.password_qwidget.text()
        #发送信号，让子线程开始登陆
        self.login_thread.start_login_signal.emit(json.dumps({"user_name": user_name,"password": password}))

        # if user_name == "admin" and password == "123456":
        #     self.textBrowser.setText("欢迎%s" % user_name)
        #     self.textBrowser.repaint()
        # else:
        #     self.textBrowser.setText("用户名或密码错误....请重试")
        #     self.textBrowser.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 展示窗口
    w.ui.show()

    app.exec()
